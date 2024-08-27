from django.contrib.gis.geos import Point
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotAcceptable

from observations.models import get_climate_station_via_coordinates, \
    get_hexagon_via_coordinates, \
    get_municipal_via_coordinates
from observations.serializers import *
from geo_util.store_geo_data import return_dgm_altitude, return_mnt_range
from observations.views.util import create_thumbnail


class CreateCategory1(CreateAPIView):
    serializer_class = Category1Serializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def perform_create(self, serializer):
        try:

            lon, lat = None, None

            if 'Lon' in serializer.validated_data:
                if serializer.validated_data['Lon']:
                    lon = float(serializer.validated_data['Lon'])

            if 'Lat' in serializer.validated_data:
                if serializer.validated_data['Lat']:
                    lat = float(serializer.validated_data['Lat'])

            if not (lat and lon):
                serializer.save(user=self.request.user)
                return
            municipal = get_municipal_via_coordinates(lat, lon)
            hexagon = get_hexagon_via_coordinates(lat, lon)
            climate_station = get_climate_station_via_coordinates(lat, lon)
            geom = Point(lon, lat)
            serializer.save(Municipal=municipal, Cell=hexagon, ClimateStation=climate_station,
                            geom=geom, user=self.request.user)
            try:
                create_thumbnail(serializer.data["Photo"].split("media/")[1])
            except:
                print("couldn't create thumbnail")
        except ObjectDoesNotExist:
            raise NotAcceptable('Coordinates are not located in Bavaria!')


class CreateCategory2(CreateAPIView):
    serializer_class = Category2Serializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def perform_create(self, serializer):
        try:

            lon, lat = None, None

            if 'Lon' in serializer.validated_data:
                if serializer.validated_data['Lon']:
                    lon = float(serializer.validated_data['Lon'])

            if 'Lat' in serializer.validated_data:
                if serializer.validated_data['Lat']:
                    lat = float(serializer.validated_data['Lat'])

            if not (lat and lon):
                serializer.save(user=self.request.user)
                return

            municipal = get_municipal_via_coordinates(lat, lon)
            hexagon = get_hexagon_via_coordinates(lat, lon)
            climate_station = get_climate_station_via_coordinates(lat, lon)
            geom = Point(lon, lat)
            serializer.save(Municipal=municipal, Cell=hexagon, ClimateStation=climate_station,
                            geom=geom, user=self.request.user)
            try:
                create_thumbnail(serializer.data["Photo"].split("media/")[1])
            except:
                print("couldn't create thumbnail")

        except ObjectDoesNotExist:
            raise NotAcceptable('Coordinates are not located in Bavaria!')


class CreateCategory3(CreateAPIView):
    serializer_class = Category3Serializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def perform_create(self, serializer):
        try:
            lon, lat = None, None

            if 'Lon' in serializer.validated_data:
                if serializer.validated_data['Lon']:
                    lon = float(serializer.validated_data['Lon'])

            if 'Lat' in serializer.validated_data:
                if serializer.validated_data['Lat']:
                    lat = float(serializer.validated_data['Lat'])

            if not (lat and lon):
                serializer.save(user=self.request.user)
                return

            municipal = get_municipal_via_coordinates(lat, lon)
            hexagon = get_hexagon_via_coordinates(lat, lon)
            climate_station = get_climate_station_via_coordinates(lat, lon)
            geom = Point(lon, lat)
            altitude = return_dgm_altitude(lat, lon)
            mountain = return_mnt_range(lat, lon)
            serializer.save(Municipal=municipal, Cell=hexagon, ClimateStation=climate_station,
                            geom=geom, Altitude_m = altitude, user=self.request.user)
            try:
                create_thumbnail(serializer.data["Photo"].split("media/")[1])
            except:
                print("couldn't create thumbnail")

        except ObjectDoesNotExist:
            raise NotAcceptable('Coordinates are not located in Bavaria!')


class CreateCategory4(CreateAPIView):
    serializer_class = Category4Serializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def perform_create(self, serializer):
        try:
            lon, lat = None, None

            if 'Lon' in serializer.validated_data:
                if serializer.validated_data['Lon']:
                    lon = float(serializer.validated_data['Lon'])

            if 'Lat' in serializer.validated_data:
                if serializer.validated_data['Lat']:
                    lat = float(serializer.validated_data['Lat'])

            if not (lat and lon):
                serializer.save(user=self.request.user)
                return

            municipal = get_municipal_via_coordinates(lat, lon)
            hexagon = get_hexagon_via_coordinates(lat, lon)
            climate_station = get_climate_station_via_coordinates(lat, lon)
            geom = Point(lon, lat)
            serializer.save(Municipal=municipal, Cell=hexagon, ClimateStation=climate_station,
                            geom=geom, user=self.request.user)
            try:
                create_thumbnail(serializer.data["Photo"].split("media/")[1])
            except:
                print("couldn't create thumbnail")

        except ObjectDoesNotExist:
            raise NotAcceptable('Coordinates are not located in Bavaria!')



