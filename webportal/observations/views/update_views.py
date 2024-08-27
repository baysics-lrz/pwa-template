# Geodjango point geometries
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.gis.geos import Point
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import UpdateView

from observations.forms import Category3Form, Category2Form, Category1Form, Category4Form
from observations.models import Category4, Category3, Category2, Category1, \
    get_municipal_via_coordinates, get_hexagon_via_coordinates, \
    get_climate_station_via_coordinates
from .util import get_map_content
from geo_util.store_geo_data import return_dgm_altitude, return_mnt_range


class UpdateCategory1(LoginRequiredMixin, UpdateView):
    model = Category1
    form_class = Category1Form
    template_name = 'update-forms/category1_update_form.html'
    success_url = '/observations/category1/show-category1-list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_map_content())
        return context

    def get(self, request, *args, **kwargs):
        # Check if the user is allowed to update the observation
        if request.user != self.get_object().user:
            return HttpResponse(status=403)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Check if the user is allowed to update the observation
        if request.user != self.get_object().user:
            return HttpResponse(status=403)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        category1 = form.save(commit=False)
        # set spatial data from the coordinates
        lon = float(form.cleaned_data['Lon'])
        lat = float(form.cleaned_data['Lat'])
        category1.Municipal = get_municipal_via_coordinates(lat, lon)
        category1.Cell = get_hexagon_via_coordinates(lat, lon)
        category1.ClimateStation = get_climate_station_via_coordinates(lat, lon)
        category1.geom = Point(lon, lat)
        category1.save()
        print('saved', category1)
        messages.success(self.request, 'Entry successfully updated!')
        return super().form_valid(form)


class UpdateCategory2(LoginRequiredMixin, UpdateView):
    model = Category2
    form_class = Category2Form
    template_name = 'update-forms/category2_update_form.html'
    success_url = '/observations/category2/show-category2-list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_map_content())
        return context

    def get(self, request, *args, **kwargs):
        # Check if the user is allowed to update the observation
        if request.user != self.get_object().user:
            return HttpResponse(status=403)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Check if the user is allowed to update the observation
        if request.user != self.get_object().user:
            return HttpResponse(status=403)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        category2 = form.save(commit=False)
        # set spatial data from the coordinates
        lon = float(form.cleaned_data['Lon'])
        lat = float(form.cleaned_data['Lat'])
        category2.Municipal = get_municipal_via_coordinates(lat, lon)
        category2.Cell = get_hexagon_via_coordinates(lat, lon)
        category2.ClimateStation = get_climate_station_via_coordinates(lat, lon)
        category2.geom = Point(lon, lat)
        category2.save()
        print('saved', category2)
        messages.success(self.request, 'Entry successfully updated!')
        return super().form_valid(form)


class UpdateCategory3(LoginRequiredMixin, UpdateView):
    model = Category3
    form_class = Category3Form
    template_name = 'update-forms/category3_update_form.html'
    success_url = '/observations/category3/show-category3-list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_map_content())
        return context

    def get(self, request, *args, **kwargs):
        # Check if the user is allowed to update the observation
        if request.user != self.get_object().user:
            return HttpResponse(status=403)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Check if the user is allowed to update the observation
        if request.user != self.get_object().user:
            return HttpResponse(status=403)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        category3 = form.save(commit=False)
        # set spatial data from the coordinates
        lon = float(form.cleaned_data['Lon'])
        lat = float(form.cleaned_data['Lat'])
        category3.Municipal = get_municipal_via_coordinates(lat, lon)
        category3.Cell = get_hexagon_via_coordinates(lat, lon)
        category3.ClimateStation = get_climate_station_via_coordinates(lat, lon)
        category3.geom = Point(lon, lat)
        category3.Altitude_m = return_dgm_altitude(lat, lon)
        category3.save()
        print('saved', category3)
        messages.success(self.request, 'Entry successfully updated!')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return redirect(self.success_url)


class UpdateCategory4(LoginRequiredMixin, UpdateView):
    model = Category4
    form_class = Category4Form
    template_name = 'update-forms/category4_update_form.html'
    success_url = '/observations/category4/show-category4-list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_map_content())
        return context

    def get(self, request, *args, **kwargs):
        # Check if the user is allowed to update the observation
        if request.user != self.get_object().user:
            return HttpResponse(status=403)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Check if the user is allowed to update the observation
        if request.user != self.get_object().user:
            return HttpResponse(status=403)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        category4 = form.save(commit=False)
        # set spatial data from the coordinates
        lon = float(form.cleaned_data['Lon'])
        lat = float(form.cleaned_data['Lat'])
        category4.Municipal = get_municipal_via_coordinates(lat, lon)
        category4.Cell = get_hexagon_via_coordinates(lat, lon)
        category4.ClimateStation = get_climate_station_via_coordinates(lat, lon)
        category4.geom = Point(lon, lat)
        # save the category4 and get to the success-url
        category4.save()
        print('saved', category4)
        messages.success(self.request, 'Entry successfully updated!')
        return super().form_valid(form)

