
# Create your views here.
import datetime

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from djangorestframework.views import View

# app specific files

from models import *
from forms import *
from django.db import transaction

@transaction.commit_on_success
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    t = get_template('depot/create_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@transaction.commit_on_success
def create_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderForm()
    t = get_template('depot/create_order.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def list_product(request):
  
    list_items = Product.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('depot/list_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def list_order(request):

    list_items = Order.objects.all()
    paginator = Paginator(list_items, 10)

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('depot/list_order.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def view_product(request, id):
    product_instance = Product.objects.get(id = id)

    t=get_template('depot/view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def view_order(request, id):
    order_instance = Order.objects.get(id=id)

    t = get_template('depot/view_order.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

@transaction.commit_on_success
def edit_product(request, id):

    product_instance = Product.objects.get(id=id)

    form = ProductForm(request.POST or None, instance = product_instance)

    if form.is_valid():
        form.save()

    t=get_template('depot/edit_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

@transaction.commit_on_success
def edit_order(request, id):
    order_instance = Order.objects.get(id=id)
    form = OrderForm(request.POST or None, instance=order_instance)

    if form.is_valid():
        form.save()

    t = get_template('depot/edit_order.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def store_view(request):
    products = Product.objects.filter(date_available__gt=datetime.datetime.now().date())\
        .order_by('-date_available')
    t = get_template('depot/store.html')
    c = RequestContext(request, locals())
    cart = request.session.get("cart",None)
    return HttpResponse(t.render(c))

def view_cart(request):
    cart = request.session.get("cart", None)
    t = get_template('depot/view_cart.html')

    if not cart:
        cart = Cart()
        request.session["cart"] = cart

    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

@transaction.commit_on_success
def add_to_cart(request, id):
    product = Product.objects.get(id = id)
    cart = request.session.get("cart", None)
    if not cart:
        cart = Cart()
        request.session["cart"] = cart
    cart.add_product(product)
    request.session["cart"] = cart
    return view_cart(request)

def clean_cart(request):
    request.session["cart"] = Cart()
    return view_cart(request)

class RESTforCart(View):
    def get(self, request, *args, **kwargs):
        return request.session['cart'].items
    def post(self, request, *args, **kwargs):
        print request.POST["product"]
        product = Product.objects.get(id=request.POST["product"])
        cart = request.session["cart"]
        cart.add_product(product)
        request.session["cart"] = cart
        return request.session["cart"].items
