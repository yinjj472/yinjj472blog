# Create your views here.
from django.http import HttpResponse
from django.template.context import RequestContext
from blog.models import Article, Category
from django.shortcuts import render_to_response
from blog.form import ArticleForm, CategoryForm
from django.template.loader import get_template
from django.db import transaction
from django.core.paginator import Paginator

def list_article(request):
    list_items = Article.objects.all()
    paginator = Paginator(list_items, 10)
    try:
        page = int(request.GET.get("page", 1))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)
    t = get_template('blog/list_article.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def view_article(request, id):
    object_id = int(id)
    article_instance = Article.objects.filter(id=object_id)
    t = get_template('blog/view_article.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

@transaction.commit_on_success
def create_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()

    t = get_template('blog/create_article.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

@transaction.commit_on_success
def edit_article(request, id):
    article_instance = Article.objects.get(id=id)
    form = ArticleForm(request.POST or None, instance=article_instance)
    if form.is_valid():
        form.save()

    t = get_template('blog/edit_article.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

@transaction.commit_on_success
def delete_article(request, id):
    Article.objects.get(id=id).delete()
    list_items = Article.objects.all()
    paginator = Paginator(list_items, 10)
    page = 1
    list_items = paginator.page(1)
    t = get_template('blog/list_article.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

@transaction.commit_on_success
def create_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid:
        form.save()
        form = CategoryForm()

    t = get_template('blog/create_category.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

@transaction.commit_on_success
def edit_category(request, id):
    category_instance = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None, instance=category_instance)
    if form.is_valid():
        form.save()

    t = get_template('blog/edit_category.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def view_category(request, id):
    category_instance = Category.objects.get(id=id)
    t = get_template('blog/view_category.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def list_category(request):
    list_items = Category.objects.all()
    paginator = Paginator(list_items, 10)

    try:
       page = int(request.GET.get("page", 1))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)
    print 1
    t = get_template('blog/list_category.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

@transaction.commit_on_success
def delete_category(request, id):
    Category.objects.get(id=id).delete()

    list_items = Category.objects.all()
    paginator = Paginator(list_items, 10)

    page = 1

    list_items = paginator.page(page)

    t = get_template('blog/list_category.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))
