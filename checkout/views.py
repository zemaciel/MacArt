from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NwNIpJrg7P3ry9omI78uxetjgZM3rvXoosSvi4e2qNwqSe2UcEGmcuB6JDi6HT1zAF3ZQqfh7BIfCoUDTpUIa8L00OMjwEYtW',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)