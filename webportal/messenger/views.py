from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import ReportMessage


class ViewReport(View):

    def get(self, request, pk, *args, **kwargs):
        try:
            report = ReportMessage.objects.get(id=pk)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)
        return render(request, 'report.html', {'report': report})
