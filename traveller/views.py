from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from guardian.decorators import permission_required_or_403
from notifications import notify
from plan.models import Plan
from django.template import loader
from traveller.models import ProfileEditForm, Traveller
from friendship.models import Friend, FriendshipRequest
import json
import os


class ProfileView(View):
    is_current_user = None
    def get(self, request , profile_id = None):
        if profile_id is None:
            self.is_current_user = True
            traveller = request.user.profile

        else:
            try:
                traveller = Traveller.objects.get(pk=profile_id)
            except:
                return HttpResponseRedirect('/login')
            if int(profile_id) == request.user.profile.id:
                self.is_current_user = True
            else:
                self.is_current_user = False

        created_plans = traveller.create_plan_set.all()
        participated_plans = traveller.participate_plan_set.all()



        context = {'traveller': traveller, 'created_plans': created_plans, 'participated_plans': participated_plans,
                    'is_current_user':self.is_current_user,}



        return render_to_response('traveller/profile.html', context, context_instance=RequestContext(request))


class PlanDetailView(View):

    def get(self, request, plan_id):
        try:
            plan = Plan.objects.get(pk=plan_id)
        except plan.DoesNotExist:
            raise Http404
        template = loader.get_template('plan/detail.html')
        context = RequestContext(request, {
            'plan': plan,
        })

        return HttpResponse(template.render(context))


class ProfileEditView(View):
    form_class = ProfileEditForm
    template_name = 'traveller/edit.html'

    def get(self, request):
        traveller = request.user.profile
        form = self.form_class(instance=traveller)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        traveller = request.user.profile
        form = self.form_class(request.POST, instance=traveller)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('.')
        return render(request, self.template_name, {'form': form})


class ProfileListView(View):
    template_name = "traveller/all_list.html"

    def get(self,request):
        all_traveller = Traveller.objects.all()

        return render(request, self.template_name, {'all_traveller': all_traveller})


class AddFriend(View):

    def get(self,request,profile_id):

        friend_asker = request.user
        friend_target = Traveller.objects.filter(pk=profile_id)[0]


        notify.send(friend_asker, recipient=friend_target.user, verb=u'sent you a friend request',
            action_object=friend_asker, description=u'',)
        Friend.objects.add_friend(friend_asker,friend_target.user)
        response_data = {'result':'success'}
        if Friend.objects.are_friends(request.user, friend_target.user) == True:
            print "friend!"
        return HttpResponse(json.dumps(response_data), content_type="application/json")


