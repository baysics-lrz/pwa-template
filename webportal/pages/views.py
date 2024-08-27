# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render

from observations.models import Category1, Category2, Category3, Category4

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        try:

                category1_list = Category1.objects.all()
                category2_list = Category2.objects.all()
                category3_list = Category3.objects.all()
                category4_list = Category4.objects.all()

                context = {
                    "category1_list": category1_list,
                    "category2_list": category2_list,
                    "category3_list": category3_list,
                    "category4_list": category4_list,
                }
                return render(request, 'home.html', context)
        except AttributeError:
            return render(request, 'home.html')


class ImpressumPageView(TemplateView):
    template_name = 'impressum.html'


class DataPolicyPageView(TemplateView):
    template_name = 'datapolicy.html'


class FAQPageView(TemplateView):
    template_name = 'faq.html'


class TermsOfUsePageView(TemplateView):
    template_name = 'terms_of_use.html'


class DownloadsPageView(TemplateView):
    template_name = 'downloads.html'



def error_500(request):
    return render(request, '500.html', status=500)

def error_404(request,  exception):
    return render(request, '404.html', status=404)

