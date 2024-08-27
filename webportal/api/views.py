from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class DocumentationShortView(TemplateView):
    template_name = 'doc_short.html'


@login_required(login_url='/accounts/login')
def show_APIDocumentation_Full(request):
    return render (request, 'doc_full.html')