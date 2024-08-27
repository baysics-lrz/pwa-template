from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .forms import ContactForm
from django.contrib import messages


# Create your views here.

def send_contact(request):
    # Sending a contact form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            template = get_template('contact_template.txt')
            context = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            }
            content = template.render(context)
            messages.success(request, 'Your message was sent successfully.')
            # Please replace here with the email address you want to use.
            try:
                send_mail("Inquiry (Your Project):" + subject, content, 'mail@mail.com', ['mail@mail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header')

            return redirect('/contact/send/')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

