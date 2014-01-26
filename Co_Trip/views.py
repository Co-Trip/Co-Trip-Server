from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.generic import TemplateView


def home(request):
    template = loader.get_template('Co_Trip/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


class AboutView(TemplateView):
    template_name = "Co_Trip/about.html"