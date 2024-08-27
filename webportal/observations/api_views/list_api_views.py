from rest_framework.generics import ListAPIView

from observations.models import Category1, Category2, Category3, Category4
from observations.serializers import *

class Category1List(ListAPIView):
    serializer_class = Category1Serializer
    permission_classes = []

    # Overwriting the get_queryset method to filter the result with the url
    def get_queryset(self):
        queryset = Category1.objects.all()
        id = self.request.query_params.get('id', None)
        category1subject = self.request.query_params.get('Category1Subject', None)
        number = self.request.query_params.get('Number', None)
        category1feature1 = self.request.query_params.get('Category1Feature1', None)
        category1feature2 = self.request.query_params.get('Category1Feature2', None)
        category1feature3 = self.request.query_params.get('Category1Feature3', None)
        observation_date = self.request.query_params.get('ObservationDate', None)
        observation_time = self.request.query_params.get('ObservationTime', None)
        municipal = self.request.query_params.get('Municipal', None)
        lat = self.request.query_params.get('Lat', None)
        lon = self.request.query_params.get('Lon', None)
        accuracy_gps = self.request.query_params.get('AccuracyGPS', None)
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        if id is not None:
            queryset = queryset.filter(id=id)
        if category1subject is not None:
            queryset = queryset.filter(Category1Subject=category1subject)
        if number is not None:
            queryset = queryset.filter(Number=number)
        if category1feature1 is not None:
            queryset = queryset.filter(Category1Feature1=category1feature1)
        if category1feature2 is not None:
            queryset = queryset.filter(Category1Feature2=category1feature2)
        if category1feature3 is not None:
            queryset = queryset.filter(Category1Feature3=category1feature3)
        if observation_date is not None:
            queryset = queryset.filter(ObservationDate=observation_date)
        if observation_time is not None:
            queryset = queryset.filter(ObservationTime=observation_time)
        if municipal is not None:
            queryset = queryset.filter(Municipal=municipal)
        if lat is not None:
            queryset = queryset.filter(Lat=lat)
        if lon is not None:
            queryset = queryset.filter(Lon=lon)
        if accuracy_gps is not None:
            queryset = queryset.filter(AccuracyGPS=accuracy_gps)
        return queryset


class Category2List(ListAPIView):
    serializer_class = Category2Serializer
    permission_classes = []

    # Overwriting the get_queryset method to filter the result with the link
    def get_queryset(self):
        queryset = Category2.objects.all()
        user = self.request.query_params.get('user', None)
        certainty = self.request.query_params.get('Certainty', None)
        category2sbuject = self.request.query_params.get('Category2Subject', None)
        Category2Feature3 = self.request.query_params.get('Category2Feature3', None)
        Category2Feature4 = self.request.query_params.get('Category2Feature4', None)
        Category2Feature5 = self.request.query_params.get('Category2Feature5', None)
        Category2Feature6 = self.request.query_params.get('Category2Feature6', None)
        Category2Feature7 = self.request.query_params.get('Category2Feature7', None)
        Category2Feature8 = self.request.query_params.get('Category2Feature8', None)
        Category2Feature1 = self.request.query_params.get('Category2Feature1', None)
        category2feature2 = self.request.query_params.get('Category2Feature2', None)
        lat = self.request.query_params.get('Lat', None)
        lon = self.request.query_params.get('Lon', None)
        accuracy_gps = self.request.query_params.get('AccuracyGPS', None)
        municipal = self.request.query_params.get('Municipal', None)
        observation_date = self.request.query_params.get('ObservationDate', None)
        id = self.request.query_params.get('id', None)


        if id is not None:
            queryset = queryset.filter(id=id)
        if certainty is not None:
            queryset = queryset.filter(Certainty=certainty)
        if category2sbuject is not None:
            queryset = queryset.filter(Category2Subject=category2sbuject)
        if user is not None:
            queryset = queryset.filter(user=user)
        if Category2Feature3 is not None:
            queryset = queryset.filter(Category2Feature3=Category2Feature3)
        if Category2Feature4 is not None:
            queryset = queryset.filter(Category2Feature4=Category2Feature4)
        if Category2Feature5 is not None:
            queryset = queryset.filter(Category2Feature5=Category2Feature5)
        if Category2Feature6 is not None:
            queryset = queryset.filter(Category2Feature6=Category2Feature6)
        if Category2Feature7 is not None:
            queryset = queryset.filter(Category2Feature7=Category2Feature7)
        if Category2Feature8 is not None:
            queryset = queryset.filter(Category2Feature8=Category2Feature8)
        if Category2Feature1 is not None:
            queryset = queryset.filter(Category2Feature1=Category2Feature1)
        if category2feature2 is not None:
            queryset = queryset.filter(Category2Feature2=category2feature2)
        if municipal is not None:
            queryset = queryset.filter(Municipal=municipal)
        if lat is not None:
            queryset = queryset.filter(Lat=lat)
        if lon is not None:
            queryset = queryset.filter(Lon=lon)
        if accuracy_gps is not None:
            queryset = queryset.filter(AccuracyGPS=accuracy_gps)
        if observation_date is not None:
            queryset = queryset.filter(ObservationDate=observation_date)
        return queryset


class Category3List(ListAPIView):
    serializer_class = Category3Serializer
    permission_classes = []

    # Overwriting the get_queryset method to filter the result with the link
    def get_queryset(self):
        queryset = Category3.objects.all()
        user = self.request.query_params.get('user', None)
        certainty = self.request.query_params.get('Certainty', None)
        category3sbuject = self.request.query_params.get('Category3Subject', None)
        id = self.request.query_params.get('id', None)
        category3feature1 = self.request.query_params.get('Category3Feature1', None)
        Category3Feature2 = self.request.query_params.get('Category3Feature2', None)
        accuracy_gps = self.request.query_params.get('AccuracyGPS', None)
        municipal = self.request.query_params.get('Municipal', None)
        lat = self.request.query_params.get('Lat', None)
        lon = self.request.query_params.get('Lon', None)
        observation_date = self.request.query_params.get('ObservationDate', None)

        if user is not None:
            queryset = queryset.filter(user=user)
        if certainty is not None:
            queryset = queryset.filter(Certainty=certainty)
        if category3sbuject is not None:
            queryset = queryset.filter(Category3Subject=category3sbuject)
        if id is not None:
            queryset = queryset.filter(id=id)
        if category3feature1 is not None:
            queryset = queryset.filter(Category3Feature1=category3feature1)
        if accuracy_gps is not None:
            queryset = queryset.filter(AccuracyGPS=accuracy_gps)
        if Category3Feature2 is not None:
            queryset = queryset.filter(Category3Feature2=Category3Feature2)
        if observation_date is not None:
            queryset = queryset.filter(ObservationDate=observation_date)
        if municipal is not None:
            queryset = queryset.filter(Municipal=municipal)
        if lat is not None:
            queryset = queryset.filter(Lat=lat)
        if lon is not None:
            queryset = queryset.filter(Lon=lon)
        if observation_date is not None:
            queryset = queryset.filter(ObservationDate=observation_date)
        return queryset


class Category4List(ListAPIView):
    serializer_class = Category4Serializer
    permission_classes = []

    # Overwriting the get_queryset method to filter the result with the link
    def get_queryset(self):
        queryset = Category4.objects.all()
        user = self.request.query_params.get('user', None)
        certainty = self.request.query_params.get('Certainty', None)
        category4sbuject = self.request.query_params.get('Category4Subject', None)
        Category4Feature1 = self.request.query_params.get('Category4Feature1', None)
        Category4Feature2 = self.request.query_params.get('Category4Feature2', None)
        Category4Feature3 = self.request.query_params.get('Category4Feature3', None)
        lat = self.request.query_params.get('Lat', None)
        lon = self.request.query_params.get('Lon', None)
        accuracy_gps = self.request.query_params.get('AccuracyGPS', None)
        municipal = self.request.query_params.get('Municipal', None)
        observation_date = self.request.query_params.get('ObservationDate', None)
        id = self.request.query_params.get('id', None)
        user = self.request.query_params.get('user', None)

        if user is not None:
            queryset = queryset.filter(user=user)
        if id is not None:
            queryset = queryset.filter(id=id)
        if certainty is not None:
            queryset = queryset.filter(Certainty=certainty)
        if category4sbuject is not None:
            queryset = queryset.filter(Category4Subject=category4sbuject)
        if user is not None:
            queryset = queryset.filter(user=user)
        if Category4Feature1 is not None:
            queryset = queryset.filter(Category4Feature1=Category4Feature1)
        if Category4Feature2 is not None:
            queryset = queryset.filter(Category4Feature2=Category4Feature2)
        if Category4Feature3 is not None:
            queryset = queryset.filter(Category4Feature3=Category4Feature3)
        if municipal is not None:
            queryset = queryset.filter(Municipal=municipal)
        if lat is not None:
            queryset = queryset.filter(Lat=lat)
        if lon is not None:
            queryset = queryset.filter(Lon=lon)
        if accuracy_gps is not None:
            queryset = queryset.filter(AccuracyGPS=accuracy_gps)
        if observation_date is not None:
            queryset = queryset.filter(ObservationDate=observation_date)
        return queryset


