from django.contrib.gis.geos import Point
from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.exceptions import PermissionDenied, NotAcceptable
from django.core.exceptions import ObjectDoesNotExist

from observations.models import get_climate_station_via_coordinates, \
    get_hexagon_via_coordinates, \
    get_municipal_via_coordinates
from observations.serializers import *
from geo_util.store_geo_data import return_dgm_altitude, return_mnt_range
from observations.views.util import create_thumbnail


class UpdateCategory1(UpdateAPIView):
    queryset = Category1.objects.all()
    serializer_class = Category1Serializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    # overwriting the update-method
    def perform_update(self, serializer):
        # performing the update only if the user is the one sending the request
        if self.request.user != self.get_object().user:
            raise PermissionDenied('You can not change entries of other users!')
        try:
            lon, lat = None, None
            if 'Lon' in serializer.validated_data:
                if serializer.validated_data['Lon']:
                    lon = float(serializer.validated_data['Lon'])
            elif self.get_object().Lon:
                lon = float(self.get_object().Lon)

            if 'Lat' in serializer.validated_data:
                if serializer.validated_data['Lat']:
                    lat = float(serializer.validated_data['Lat'])
            elif self.get_object().Lat:
                lat = float(self.get_object().Lat)

            if not (lat and lon):
                serializer.save()
                return

            municipal = get_municipal_via_coordinates(lat, lon)
            hexagon = get_hexagon_via_coordinates(lat, lon)
            climate_station = get_climate_station_via_coordinates(lat, lon)
            geom = Point(lon, lat)
            serializer.save(Municipal=municipal, Cell=hexagon, ClimateStation=climate_station,
                            geom=geom)
            try:
                create_thumbnail(serializer.data["Photo"].split("media/")[1])
            except:
                print("couldn't create thumbnail")

        except ObjectDoesNotExist:
            raise NotAcceptable('Coordinates are not located in Bavaria!')


class UpdateCategory2(UpdateAPIView):
    queryset = Category2.objects.all()
    serializer_class = Category2Serializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    # overwriting the update-method
    def perform_update(self, serializer):
        # performing the update only if the user is the one sending the request
        if self.request.user != self.get_object().user:
            raise PermissionDenied('You can not change entries of other users!')
        try:
            lon, lat = None, None
            if 'Lon' in serializer.validated_data:
                if serializer.validated_data['Lon']:
                    lon = float(serializer.validated_data['Lon'])
            elif self.get_object().Lon:
                lon = float(self.get_object().Lon)

            if 'Lat' in serializer.validated_data:
                if serializer.validated_data['Lat']:
                    lat = float(serializer.validated_data['Lat'])
            elif self.get_object().Lat:
                lat = float(self.get_object().Lat)

            if not (lat and lon):
                serializer.save()
                return

            municipal = get_municipal_via_coordinates(lat, lon)
            hexagon = get_hexagon_via_coordinates(lat, lon)
            climate_station = get_climate_station_via_coordinates(lat, lon)
            geom = Point(lon, lat)
            serializer.save(Municipal=municipal, Cell=hexagon, ClimateStation=climate_station,
                            geom=geom)
            try:
                create_thumbnail(serializer.data["Photo"].split("media/")[1])
            except:
                print("couldn't create thumbnail")

        except ObjectDoesNotExist:
            raise NotAcceptable('Coordinates are not located in Bavaria!!')


class UpdateCategory3(UpdateAPIView):
    queryset = Category3.objects.all()
    serializer_class = Category3Serializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    # overwriting the update-method
    def perform_update(self, serializer):
        # performing the update only if the user is the one sending the request
        if self.request.user != self.get_object().user:
            raise PermissionDenied('You can not change entries of other users!')
        try:
            lon, lat = None, None
            if 'Lon' in serializer.validated_data:
                if serializer.validated_data['Lon']:
                    lon = float(serializer.validated_data['Lon'])
            elif self.get_object().Lon:
                lon = float(self.get_object().Lon)

            if 'Lat' in serializer.validated_data:
                if serializer.validated_data['Lat']:
                    lat = float(serializer.validated_data['Lat'])
            elif self.get_object().Lat:
                lat = float(self.get_object().Lat)

            if not (lat and lon):
                serializer.save()
                return

            municipal = get_municipal_via_coordinates(lat, lon)
            hexagon = get_hexagon_via_coordinates(lat, lon)
            climate_station = get_climate_station_via_coordinates(lat, lon)
            geom = Point(lon, lat)
            altitude = return_dgm_altitude(lat, lon)
            mountain = return_mnt_range(lat, lon)
            serializer.save(Municipal=municipal, Cell=hexagon, ClimateStation=climate_station,
                            geom=geom, Altitude_m= altitude)
            try:
                create_thumbnail(serializer.data["Photo"].split("media/")[1])
            except:
                print("couldn't create thumbnail")

        except ObjectDoesNotExist:
            raise NotAcceptable('Coordinates are not located in Bavaria!')


class UpdateCategory4(UpdateAPIView):
    queryset = Category4.objects.all()
    serializer_class = Category4Serializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    # overwriting the update-method
    def perform_update(self, serializer):
        # performing the update only if the user is the one sending the request
        if self.request.user != self.get_object().user:
            raise PermissionDenied('You can not change entries of other users!')
        try:
            lon, lat = None, None
            if 'Lon' in serializer.validated_data:
                if serializer.validated_data['Lon']:
                    lon = float(serializer.validated_data['Lon'])
            elif self.get_object().Lon:
                lon = float(self.get_object().Lon)

            if 'Lat' in serializer.validated_data:
                if serializer.validated_data['Lat']:
                    lat = float(serializer.validated_data['Lat'])
            elif self.get_object().Lat:
                lat = float(self.get_object().Lat)

            if not (lat and lon):
                serializer.save()
                return

            municipal = get_municipal_via_coordinates(lat, lon)
            hexagon = get_hexagon_via_coordinates(lat, lon)
            climate_station = get_climate_station_via_coordinates(lat, lon)
            geom = Point(lon, lat)
            serializer.save(Municipal=municipal, Cell=hexagon, ClimateStation=climate_station,
                            geom=geom)
            try:
                create_thumbnail(serializer.data["Photo"].split("media/")[1])
            except:
                print("couldn't create thumbnail")

        except ObjectDoesNotExist:
            raise NotAcceptable('Coordinates are not located in Bavaria!')