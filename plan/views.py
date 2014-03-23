import json
from django.forms import HiddenInput

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from django.utils.datetime_safe import datetime
from django.views.generic import View
from city.models import Province
from friendship.models import Follow
from plan.form import PlanForm
from plan.models import Plan, Event
from django.template import loader, RequestContext

from traveller.models import Traveller
from django.contrib.auth.models import Group, AnonymousUser
from guardian.shortcuts import assign_perm
from guardian.decorators import permission_required_or_403


class PlanCreateStep1View(View):
    template_name = 'plan/create_step1.html'

    def get(self, request):


        primary_form = PlanForm(current_user=request.user)
        followers = Follow.objects.followers(request.user)
        followings = Follow.objects.following(request.user)
        participants_choice_list = list(set(followers+followings))
        province_list = Province.objects.all()

        return render(request, self.template_name, {'form': primary_form, 'friends':participants_choice_list, 'province_list':province_list})

    def post(self, request):

        form = PlanForm(current_user=request.user, data=request.POST)
        followers = Follow.objects.followers(request.user)
        followings = Follow.objects.following(request.user)
        participants_choice_list = list(set(followers+followings))
        if form.is_valid():

            plan = form.save(commit=False)
            plan.create_time = datetime.now()
            plan.creator = request.user.profile
            try:
                participants_list = request.POST['participants']
            except:
                participants_list=[]
            start_date = form.cleaned_data['leaving_date']
            end_date = form.cleaned_data['return_date']
            delta_days = end_date - start_date

            plan.days = delta_days.days + 1
            plan.participants_number = len(participants_list)
            print len(participants_list)
            print participants_list

            plan.save()
            form.save_m2m()
            plan.participants = participants_list
            plan.save()
            # form.save()

            if request.user.profile.city is None:
                traveller = Traveller.objects.filter(id=request.user.profile.id)[0]

                traveller.city = plan.home_city
                print request.user.profile
                traveller.save()


            if plan.is_public is True:
                group = Group.objects.get(name='all_users')
                assign_perm('view_plan_permission', group, plan)
                assign_perm('view_plan_permission', AnonymousUser(), plan)
            else:
                assign_perm('view_plan_permission', plan.creator.user, plan)
                for p in plan.participants.all():
                    assign_perm('view_plan_permission', p.user, plan)

            #assign edit permission
            assign_perm('edit_plan_permission', plan.creator.user, plan)

            if plan.participants_can_edit is True:
                for p in plan.participants.all():
                    assign_perm('edit_plan_permission', p.user, plan)

            return HttpResponseRedirect('/plan/edit/' + str(plan.id)+"/")
        return render(request, self.template_name, {'form': form,  'friends':participants_choice_list})


class PlanCreateStep2View(View):
    template_name = 'plan/create_step2.html'

    def get(self, request, plan_id):

        main_plan = Plan.objects.get(id = plan_id)
        return render_to_response(self.template_name, context_instance=RequestContext(request),
                                  dictionary={'main_plan':main_plan})


class PlanEventView(View):

    def get(self, request, plan_id):
        events = []
        plan = Plan.objects.get(id=plan_id)
        event_set = plan.event_set
        for e in event_set.all():
            d = {}
            d['id'] = e.id
            d['title'] = e.title
            d['description'] = e.description
            d['spend'] = e.spend
            d['start'] = e.start_time
            d['end'] = e.end_time
            d['class'] = e.event_class
            events.append(d)
        to_json = {"success": 1,"result":events}
        return HttpResponse(json.dumps(to_json), mimetype='application/json')

    def post(self, request, plan_id):

        plan = Plan.objects.get(id=plan_id)
        event = Event()

        event.start_time = request.POST['start']

        event.end_time = request.POST['end']
        event.title = request.POST['title']
        event.description = request.POST['description']
        event.spend = request.POST['spend']
        event.event_class = request.POST['class']
        event.main_plan = plan
        event.save()
        to_json = {"success": 1}
        return HttpResponse(json.dumps(to_json), mimetype='application/json')

class PlanEditView(View):
    form_class = PlanForm
    template_name = 'plan/edit.html'


    def get(self, request, plan_id):
        plan = Plan.objects.get(id=plan_id)
        form = self.form_class(instance=plan, current_user=request.user)

        if request.user != plan.creator.user:
            form.fields['participants_can_edit'].widget = HiddenInput()

        return render(request, self.template_name, {'form': form})


    def post(self, request, plan_id):
        plan = Plan.objects.get(id=plan_id)
        form = self.form_class(current_user=request.user, data=request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('edit/success')
        return render(request, self.template_name, {'form': form})


class PlanDetailView(View):
    form_class = PlanForm
    template_name = 'plan/detail.html'


    def get(self, request, plan_id):
        plan = Plan.objects.get(id=plan_id)
        form = self.form_class(instance=plan, current_user=request.user)

        if request.user != plan.creator.user:
            form.fields['participants_can_edit'].widget = HiddenInput()

        return render(request, self.template_name, {'form': form})


def edit_success(request, plan_id):
    return HttpResponse(render(request, 'plan/success.html'))


def create_success(request):
    return HttpResponse(render(request, 'plan/success.html'))


def explore(request):
    plan_list = Plan.objects.exclude(is_public=False)
    template = loader.get_template('plan/explore_plan.html')
    context = RequestContext(request, {
        'plan_list': plan_list,
    })
    return HttpResponse(template.render(context))


@permission_required_or_403('plan.view_plan_permission', (Plan, 'id', 'plan_id'))
def detail(request, plan_id):
    try:
        main_plan = Plan.objects.get(pk=plan_id)
    except main_plan.DoesNotExist:
        raise Http404

    return render_to_response('plan/detail.html', context_instance=RequestContext(request),
                                  dictionary={'main_plan':main_plan})



