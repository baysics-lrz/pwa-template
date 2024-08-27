from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.gis.geos import Point
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView

from observations.forms import Category1Form, Category3Form, Category2Form, Category4Form
from observations.models import Category1, Category2, Category3, Category4, \
    get_municipal_via_coordinates, get_hexagon_via_coordinates, \
    get_climate_station_via_coordinates
from .util import get_map_content
from geo_util.store_geo_data import return_dgm_altitude, return_mnt_range


class CreateCategory1(LoginRequiredMixin, CreateView):
    """
    View to create a category1-observation
    """

    model = Category1
    form_class = Category1Form
    template_name = 'creation-forms/category1_create_form.html'
    success_url = '/observations/make-entry'
    login_url = '/accounts/login/'

    # get context for the map entries
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_map_content())
        return context

    def form_valid(self, form):
        # set the user-atribute to the currently logged-in user
        form.cleaned_data['user'] = self.request.user
        category1 = Category1(**form.cleaned_data)

        # set spatial data from the coordinates
        lon = float(form.cleaned_data['Lon'])
        lat = float(form.cleaned_data['Lat'])
        category1.Municipal = get_municipal_via_coordinates(lat, lon)
        category1.Cell = get_hexagon_via_coordinates(lat, lon)
        category1.ClimateStation = get_climate_station_via_coordinates(lat, lon)
        category1.geom = Point(lon, lat)
        # save the category1 and get to the success-url
        category1.save()
        # includes creating thumbnails for observation photos.
        messages.success(self.request, 'Entry uploaded successfully!')
        return redirect(self.success_url)


class CreateCategory2(LoginRequiredMixin, CreateView):
    """
    View to create a Category2-observation
    """
    model = Category2
    form_class = Category2Form
    template_name = 'creation-forms/category2_create_form.html'
    success_url = '/observations/make-entry'
    login_url = '/accounts/login/'

    # get context for the map entries
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_map_content())
        return context

    def form_valid(self, form):
        # set the user-atribute to the currently logged-in user
        form.cleaned_data['user'] = self.request.user
        category2 = Category2(**form.cleaned_data)

        # set spatial data from the coordinates
        lon = float(form.cleaned_data['Lon'])
        lat = float(form.cleaned_data['Lat'])
        category2.Municipal = get_municipal_via_coordinates(lat, lon)
        category2.Cell = get_hexagon_via_coordinates(lat, lon)
        category2.ClimateStation = get_climate_station_via_coordinates(lat, lon)
        category2.geom = Point(lon, lat)
        # save the category2 and get to the success-url
        category2.save()
        # includes creating thumbnails for observation photos.
        messages.success(self.request, 'Entry uploaded successfully!')
        return redirect(self.success_url)


class CreateCategory3(LoginRequiredMixin, CreateView):
    """
    View to create a Category3-observation
    """
    model = Category3
    form_class = Category3Form
    template_name = 'creation-forms/category3_create_form.html'
    success_url = '/observations/make-entry'
    login_url = '/accounts/login/'

    # get context for the map entries
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_map_content())
        return context

    def form_valid(self, form):
        # set the user-atribute to the currently logged-in user
        form.cleaned_data['user'] = self.request.user
        category3 = Category3(**form.cleaned_data)

        # set spatial data from the coordinates
        lon = float(form.cleaned_data['Lon'])
        lat = float(form.cleaned_data['Lat'])
        category3.Municipal = get_municipal_via_coordinates(lat, lon)
        category3.Cell = get_hexagon_via_coordinates(lat, lon)
        category3.ClimateStation = get_climate_station_via_coordinates(lat, lon)
        category3.geom = Point(lon, lat)
        category3.Altitude_m = return_dgm_altitude(lat, lon)
        category3.MountainRange = return_mnt_range(lat, lon)
        # save the category3 and get to the success-url
        category3.save()
        # includes creating thumbnails for observation photos.
        messages.success(self.request, 'Entry uploaded successfully!')
        return redirect(self.success_url)


class CreateCategory4(LoginRequiredMixin, CreateView):
    """
    View to create a category4-observation
    """

    model = Category4
    form_class = Category4Form
    template_name = 'creation-forms/category4_create_form.html'
    success_url = '/observations/make-entry'
    login_url = '/accounts/login/'

    # get context for the map entries
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_map_content())
        return context

    def form_valid(self, form):
        # set the user-atribute to the currently logged-in user
        form.cleaned_data['user'] = self.request.user
        category4 = Category4(**form.cleaned_data)

        # set spatial data from the coordinates
        lon = float(form.cleaned_data['Lon'])
        lat = float(form.cleaned_data['Lat'])
        category4.Municipal = get_municipal_via_coordinates(lat, lon)
        category4.Cell = get_hexagon_via_coordinates(lat, lon)
        category4.ClimateStation = get_climate_station_via_coordinates(lat, lon)
        category4.geom = Point(lon, lat)
        # save the category4 and get to the success-url
        category4.save()
        # includes createing thumbnails for observation photos.
        messages.success(self.request, 'Entry uploaded successfully!')
        return redirect(self.success_url)



