from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
	# Contact form
	name = forms.CharField(max_length=20, required=True)
	email = forms.EmailField(required=True)
	subject = forms.CharField(max_length=30, required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)
	captcha = CaptchaField(label='Please enter the characters shown.')