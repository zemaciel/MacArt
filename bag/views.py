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

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    if 'product_finish' in request.POST:
        finish = request.POST['product_finish']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    if finish:
        if item_id in list(bag.keys()):
            if 'items_by_finish' in bag[item_id]:
                if finish in bag[item_id]['items_by_finish'].keys():
                    bag[item_id]['items_by_finish'][finish] += quantity
                else:
                    bag[item_id]['items_by_finish'][finish] = quantity
            else:
                bag[item_id]['items_by_finish'] = {finish: quantity}
        else:
            bag[item_id] = {'items_by_finish': {finish: quantity}}

    request.session['bag'] = bag
    return redirect(redirect_url)
