from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import FAQEntry
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FAQForm


def FAQList(request):
    """ A view to show all Questions and Answers """

    faqs = FAQEntry.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'faq/faq.html', context)


@login_required
def add_faq(request):
    """ Add a FAQ Entry """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save()
            messages.success(request, 'Successfully added entry!')
            return redirect(reverse('FAQList'))
        else:
            messages.error(request, 'Error, check if the form is valid.')
    else:
        form = FAQForm()

    template = 'faq/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_faq(request, faq_id):
    """ Edit a FAQ Entry """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))
    faq = get_object_or_404(FAQEntry, pk=faq_id)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the entry!')
            return redirect(reverse('FAQList'))
        else:
            messages.error(request, 'Error, check if the form is valid.')
    else:
        form = FAQForm(instance=faq)
        messages.info(request, f'You are editing {faq.question}')

    template = 'faq/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """ Delete a FAQ entry from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))
    faq = get_object_or_404(FAQEntry, pk=faq_id)
    faq.delete()
    messages.success(request, 'Entry deleted!')
    return redirect(reverse('FAQList'))
