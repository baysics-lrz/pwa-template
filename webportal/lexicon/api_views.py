from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import json


class Category1Lexicon(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        subject_name = self.request.query_params.get('SubjectName', None)
        json_file = open('lexicon/lexicon-files/lexicon_category1.json')
        lexicon_list = json.load(json_file)
        subject_info = None
        for entry in lexicon_list:
            if entry['SubjectName'] == subject_name:
                subject_info = entry
                break
        if not subject_info:
            return HttpResponse(status=404)
        return Response(subject_info)


class Category2Lexicon(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        subject_name = self.request.query_params.get('SubjectName', None)
        json_file = open('lexicon/lexicon-files/lexicon_category2.json')
        lexicon_list = json.load(json_file)
        subject_info = None
        for entry in lexicon_list:
            if entry['SubjectName'] == subject_name:
                subject_info = entry
                break
        if not subject_info:
            return HttpResponse(status=404)
        return Response(subject_info)


class Category3Lexicon(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        subject_name = self.request.query_params.get('SubjectName', None)
        json_file = open('lexicon/lexicon-files/lexicon_category3.json')
        lexicon_list = json.load(json_file)
        subject_info = None
        for entry in lexicon_list:
            if entry['SubjectName'] == subject_name:
                subject_info = entry
                break
        if not subject_info:

            return HttpResponse(status=404)
        return Response(subject_info)


class Category4Lexicon(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        subject_name = self.request.query_params.get('SubjectName', None)
        json_file = open('lexicon/lexicon-files/lexicon_category4.json')
        lexicon_list = json.load(json_file)
        subject_info = None
        for entry in lexicon_list:
            if entry['SubjectName'] == subject_name:
                subject_info = entry
                break
        if not subject_info:
            return HttpResponse(status=404)
        return Response(subject_info)
