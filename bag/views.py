from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    finish = None

    if 'product_size' and product_finish in request.POST:
        size = request.POST['product_size']
        finish = request.POST['product_finish']
    bag = request.session.get('bag', {})

    if size and finish:
        if item_id in list(bag.keys()):
            if 'items' in bag[item_id]:
                bag[item_id]['items']['quantity'] += quantity
                if size:
                    bag[item_id]['items']['size'] = size
                if finish:
                    bag[item_id]['items']['finish'] = finish
            else:
                bag[item_id]['items'] = {
                    'quantity': quantity,
                    'size': size,
                    'finish': finish
                }
        else:
            bag[item_id] = {'items': {
                'quantity': quantity,
                'size': size,
                'finish': finish
            }}
    else:
        if item_id in list(bag.keys()):
            bag[item_id]['quantity'] += quantity
        else:
            bag[item_id] = {'quantity': quantity}

    request.session['bag'] = bag
    return redirect(redirect_url)
