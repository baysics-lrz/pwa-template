from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DeleteView
from django.contrib.auth import authenticate, login
from .models import User
from .forms import RegisterUserForm, EditUserForm, EditEmailForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

# Create your views here.



class ProfilePageView(LoginRequiredMixin, TemplateView):
    # Profile page view
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'profile.html'


class DeleteAccountView(LoginRequiredMixin, DeleteView):
    # Account deletion view
    model = User
    template_name = 'delete_account.html'

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        old_email = user.email
        user.is_active = False
        user.email = 'Anonymous' + str(uuid.uuid4())
        user.username = 'deleted_user_' + str(uuid.uuid4())
        user.password = str(uuid.uuid4())
        user.last_login = '1111-11-11'
        user.date_joined = '1111-11-11'
        user.save()
        return HttpResponseRedirect('/accounts/logout')


def register_user(request):
    # User registration view
    if request.method == 'POST':
        form = RegisterUserForm(request.POST, prefix='user')
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'], )
            login(request, new_user)
            return redirect('/accounts/profile')
    else:
        form = RegisterUserForm(prefix='user')
    context = {
        'form': form,
    }
    return render(request, 'register_user.html', context)


@login_required(login_url='/accounts/login')
def edit_username(request):
    # Enable user to edit username and email address
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        form = EditUserForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'edit_username.html', context)


@login_required(login_url='/accounts/login')
def edit_emailaddress(request):
    # Enable user to edit username and email address
    if request.method == 'POST':
        form = EditEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        form = EditEmailForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'edit_emailaddress.html', context)
