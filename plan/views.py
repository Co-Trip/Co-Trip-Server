from django.forms import HiddenInput
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.views.generic import View
from friendship.models import Friend
from plan.models import Plan, PlanForm
from django.template import loader, RequestContext

from traveller.models import Traveller
from django.contrib.auth.models import Group, User, AnonymousUser
from guardian.shortcuts import assign_perm
from guardian.decorators import permission_required_or_403


class PlanCreateView(View):

    form_class = PlanForm
    template_name = 'plan/create.html'

    def get(self, request):

        form = self.form_class(current_user=request.user)
        print form.fields['title'].widget.__dict__
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(current_user=request.user, data=request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.create_time = datetime.now()
            plan.creator = request.user.profile
            plan.save()
            form.save_m2m()

            if request.user.profile.city is None:

                traveller = Traveller.objects.filter(id=request.user.profile.id)[0]

                traveller.city = plan.home_city
                print request.user.profile
                traveller.save()

            #assign view permission
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

            #plan.save()
            return HttpResponseRedirect('success/')
        return render(request, self.template_name, {'form': form})


class PlanEditView(View):
    form_class = PlanForm
    template_name = 'plan/edit.html'


    def get(self, request, plan_id):
        plan = Plan.objects.get(id=plan_id)
        form = self.form_class(instance=plan, current_user=request.user.profile)
        #
        #Found a bug here.
        #user1 create a plan, user 2 is participant
        #when user2 edit the plan, he will not see user1 as a participant
        #maybe should display the creator
        #and allow participants to be empty
        if request.user != plan.creator.user:
            form.fields['participants_can_edit'].widget = HiddenInput()

        return render(request, self.template_name, {'form': form})



    def post(self, request, plan_id):
        plan = Plan.objects.get(id=plan_id)
        form = self.form_class(current_user=request.user.profile, data=request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('edit/success')
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
        plan = Plan.objects.get(pk=plan_id)
    except plan.DoesNotExist:
        raise Http404
    template = loader.get_template('plan/detail.html')
    context = RequestContext(request,{
        'plan': plan,
        })

    return HttpResponse(template.render(context))






