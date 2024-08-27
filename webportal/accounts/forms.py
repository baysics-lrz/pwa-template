from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import User


class RegisterUserForm(UserCreationForm):
    # Form for user registration
    email = forms.EmailField(required=True, label='Email')
    
    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email exists")
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username exists")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'name_agreement')


class EditUserForm(UserChangeForm):
    # Edit form for user information

    class Meta:
        model = User
        fields = ('username', 'email', 'name_agreement')


class EditEmailForm(UserChangeForm):
    # Edit form for user information


    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already registered")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('email',)
