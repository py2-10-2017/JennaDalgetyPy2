from django.shortcuts import render
from decimal import Decimal

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    request.session["items"] = [
        {"product_name": "Dojo Tshirt", "product_price": 19.99, "product_id": 100},
        {"product_name": "Dojo Sweater", "product_price": 29.99, "product_id": 200},
        {"product_name": "Dojo Cup", "product_price": 4.99, "product_id": 300},
        {"product_name": "Algorithm Book", "product_price": 49.99, "product_id": 400}
    ]
    context = {
        "items" : request.session["items"]
    }
    return render(request, "index.html", context)

def buy(request):
    try:
        request.session["product_count"]
        request.session["product_sum"]
    except:
        if not "product_sum" in request.session:
           request.session["product_sum"] = 0
        if not "product_count" in request.session:
           request.session["product_count"] = 0
    for product_type in request.session["items"]:
        if int(product_type["product_id"]) == int(request.POST["product_id"]):
                print product_type["product_id"]
                print request.POST["product_id"]
                request.session["cost"] = int(request.POST["quantity"]) * int(product_type["product_price"])
    request.session["product_count"] += int(request.POST["quantity"])
    request.session["product_sum"] += request.session["cost"]

    
    return redirect("/checkout")


def checkout(request):
    context = {
        "product_count": request.session["product_count"],
        "product_sum": request.session["product_sum"],
        "sale_total": request.session["cost"]
    }
    return render(request, "checkout.html", context)


def clear(request):
    request.session.flush()
    return redirect("/")