from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from guardian.decorators import permission_required_or_403
from plan.models import Plan
from django.template import loader
from traveller.models import ProfileEditForm


class ProfileView(View):
    def get(self, request):
        traveller = request.user.get_profile()
        created_plans = traveller.create_plan_set.all()
        participated_plans = traveller.participate_plan_set.all()
        friends = traveller.friends.all()
        #print traveller.create_plan_set.all()
        context = {'traveller': traveller, 'created_plans': created_plans, 'participated_plans': participated_plans,
                   'friends': friends}

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