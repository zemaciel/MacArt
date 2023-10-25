from django.shortcuts import render
from .models import FAQEntry
from django.contrib import messages


def FAQList(request):
    """ A view to show all Questions and Answers """

    faqs = FAQEntry.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'faq/faq.html', context)
