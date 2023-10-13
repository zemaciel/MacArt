from django.shortcuts import render

from .forms import ContactForm

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def contact(request):
    """View to the contact page (from: youtu.be/dnhEnF7_RyM) """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('the form was valid')

            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})

