from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from django.views.generic import TemplateView


def home(request):

    if request.user.id >= 0:
        return HttpResponse(render(request, 'Co_Trip/index.html'))
    else:
        return HttpResponse(render(request, 'Co_Trip/public_index.html'))


class AboutView(TemplateView):
    template_name = "Co_Trip/about.html"

def permission_denied_view(TemplateView):
    return render_to_response("Co_Trip/403.html")
