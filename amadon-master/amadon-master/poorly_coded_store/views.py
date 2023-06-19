from django.shortcuts import render ,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


# def checkout(request):
    
#     quantity_from_form = int(request.POST["quantity"])
#     price_from_form = float(request.POST["price"])
#     total_charge = quantity_from_form * price_from_form
#     context = {
#         "quantity_from_form" : quantity_from_form,
#         "price_from_form" : price_from_form,
#         "total_charge" : total_charge,
#     }
#     print("Charging credit card...")
#     Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
#     return render(request, "store/checkout.html",context)

def checkout(request):
    
    prod_id =request.POST["price_pro"]
    request.session['price'] = float(Product.objects.get(id=prod_id).price)
    request.session['quantity'] = int(request.POST["quantity"])
    request.session['total_price'] =  request.session['quantity']*  request.session['price']
    Order.objects.create(quantity_ordered=request.session['quantity'],total_price=request.session['total_price'])
    return redirect("/display")


def display(request):
    context = {
        'total_price': request.session['total_price'],
        'quantity': request.session['quantity'],
        'price': request.session['price']
    }
    return render(request, "store/checkout.html", context)