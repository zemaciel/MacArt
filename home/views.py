from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm


def index(request):
    return render(request, 'home/index.html')


def emailsent(request):
    """ A view to display the 'email sent' confirmation page """
    return render(request, 'home/emailsent.html')


def contact(request):
    """ View to the contact page (from: youtu.be/dnhEnF7_RyM) """
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('home/emails/contactform.html', {
                'name': name,
                'email': email,
                'content': content,
            })

            send_mail('The contact Form subject', 'This is the message',
                      'settings.DEFAULT_FROM_EMAIL', ['noreply@macart.com'], html_message=html)

            return redirect('emailsent')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})
