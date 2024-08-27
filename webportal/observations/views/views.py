# Geodjango point geometries
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView, DeleteView

from observations.models import Category1, Category2, Category3, Category4, \
    get_category1_ranking, get_category2_ranking, get_category3_ranking, get_category4_ranking


class SelectionPageView(LoginRequiredMixin, TemplateView):
    template_name = 'selection.html'


@login_required(login_url='/accounts/login')
def show_category1_list(request):
    category1s = Category1.objects.filter(ObservationDate__lte=timezone.now(), user=request.user).order_by('ObservationDate')
    return render(request, 'lists/show_category1_list.html', {'category1s': category1s})


@login_required(login_url='/accounts/login')
def show_category2_list(request):
    category2s= Category2.objects.filter(ObservationDate__lte=timezone.now(), user=request.user).order_by('ObservationDate')
    return render(request, 'lists/show_category2_list.html', {'category2s': category2s})


@login_required(login_url='/accounts/login')
def show_category3_list(request):
    category3s = Category3.objects.filter(ObservationDate__lte=timezone.now(), user=request.user).order_by('ObservationDate')
    return render(request, 'lists/show_category3_list.html', {'category3s': category3s})


@login_required(login_url='/accounts/login')
def show_category4_list(request):
    category4s = Category4.objects.filter(ObservationDate__lte=timezone.now(), user=request.user).order_by('ObservationDate')
    return render(request, 'lists/show_category4_list.html', {'category4s': category4s})


@login_required(login_url='/accounts/login')
def show_my_list(request):
    category1s = Category1.objects.filter(ObservationDate__lte=timezone.now(), user=request.user).order_by('ObservationDate')
    category2s = Category2.objects.filter(ObservationDate__lte=timezone.now(), user=request.user).order_by('ObservationDate')
    category3s = Category3.objects.filter(ObservationDate__lte=timezone.now(), user=request.user).order_by('ObservationDate')
    category4s = Category4.objects.filter(ObservationDate__lte=timezone.now(), user=request.user).order_by('ObservationDate')

    return render(request, 'lists/MyEntries.html',
                  {'category1s': category1s, 'category2s': category2s, 'category3s': category3s,
                   'category4s': category4s})


class OverviewPageView(TemplateView):
    # Template view for successful entries
    def get(self, request, *args, **kwargs): # "get" ist vordefiniert und kann request haben
        try:
                category1_list = Category1.objects.all().filter(user_id=request.user) # All entries from the model where user is current user
                category2_list = Category2.objects.all().filter(user_id=request.user)
                category3_list = Category3.objects.all().filter(user_id=request.user)
                category4_list = Category4.objects.all().filter(user_id=request.user)
                active_user = request.user.id
                context = {
                    "category1_list": category1_list,
                    "category2_list": category2_list,
                    "category3_list": category3_list,
                    "category4_list": category4_list,
                    "active_user": active_user,
                    "allentries": category1_list.count()
                                  + category2_list.count()
                                  + category3_list.count()
                                  + category4_list.count(),
                }
                return render(request, 'overview.html', context)  # get "render"
        except AttributeError:
            return render(request, 'overview.html')


@staff_member_required
def flagged_entries(request):
    category1s = Category1.objects.filter(ObservationDate__lte=timezone.now()).order_by('ObservationDate').exclude(Flag=None)
    category2s = Category2.objects.filter(ObservationDate__lte=timezone.now()).order_by('ObservationDate').exclude(Flag=None)
    category3s = Category3.objects.filter(ObservationDate__lte=timezone.now()).order_by('ObservationDate').exclude(Flag=None)
    category4s = Category4.objects.filter(ObservationDate__lte=timezone.now()).order_by('ObservationDate').exclude(Flag=None)

    return render(request, 'lists/flagged_entries.html',
                  {'category1s': category1s, 'category2s': category2s, 'category3s': category3s,
                   'category4s': category4s})


class RankView(TemplateView):
    # Template view for successful entries
    template_name = 'rank.html'

    # load context for the ranking
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # loading the first 5 users each into context
        # fix notification_count
        context['category1_ranking'] = get_category1_ranking()
        context['category2_ranking'] = get_category2_ranking()
        context['category3_ranking'] = get_category3_ranking()
        context['category4_ranking'] = get_category4_ranking()
        return context


class ChallengesPageView(TemplateView):
    # Template view for successful entries
    def get(self, request, *args, **kwargs): # "get" ist vordefiniert und kann request haben
        category1_list = Category1.objects.all().filter(user_id=request.user)
        category2_list = Category2.objects.all().filter(user_id=request.user)
        category3_list = Category3.objects.all().filter(user_id= request.user)
        category4_list = Category4.objects.all().filter(user_id= request.user)
        active_user = request.user.username
        traveler_category1 = category1_list.filter(user_id= request.user).values_list('Municipal')
        traveler_category2 = category2_list.filter(user_id= request.user).values_list('Municipal')
        traveler_category3 = category3_list.filter(user_id= request.user).values_list('Municipal')
        traveler_category4 = category4_list.filter(user_id= request.user).values_list('Municipal')

        context = {
                    "category1_list": category1_list,
                    "category2_list": category2_list,
                    "category3_list": category3_list,
                    "category4_list": category4_list,
                    "active_user": active_user,
                    "allentries": category1_list.count()
                                  + category2_list.count()
                                  + category3_list.count()
                                  + category4_list.count(),
                    "category1listnames": category1_list.distinct('Category1Subject'),
                    "category2listnames": category2_list.distinct('Category2Subject'),
                    "category3listnames": category3_list.distinct('Category3Subject'),
                    "category4listnames": category4_list.distinct('Category4Subject'),
                    "traveler": traveler_category1.union(traveler_category2, traveler_category3, traveler_category4)
                        .count(),
                    }
        return render(request, 'challenges.html', context)
