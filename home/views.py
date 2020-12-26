from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
# Create your views here.
from home.forms import SearchForm
from home.models import Setting
from product.models import Category, Product, Images


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('id')[:4] #last 4 product
    products_latest = Product.objects.all().order_by('-id')[:8] #last 4 product
    products_picked = Product.objects.all().order_by('?')[:8]
    # blog = Blog.objects.all().order_by('?')[:4] #Random selected 4 product
    page = "home"
    context = {
        'setting': setting,
        'page':page,
        'products_slider': products_slider,
        'products_latest': products_latest,
        'products_picked': products_picked,
        'category':category,
        # 'blog':blog,

    }
    return render(request, 'index.html',context)



def category_products(request, id, slug):
    category=Category.objects.all()
    products_latest = Product.objects.all().order_by('-id')[:8] #last 4 product
    catdata =Category.objects.get(pk=id)
    products=Product.objects.filter(category_id=id)
    context = {
        'products':products,
        'category':category,
        'catdata':catdata,
        'products_latest': products_latest,
    }
    return render(request, 'category_products.html', context)



def product_detail(request, id, slug):
    category=Category.objects.all()
    products_picked = Product.objects.all().order_by('?')[:4] #last 4 product
    products_latest = Product.objects.all().order_by('-id')[:8] #last 4 product
    product=Product.objects.get(pk=id)
    images=Images.objects.filter(product_id=id)
    # comments = Comment.objects.filter(product_id=id, status='True')
    context = {
        'product': product,
        'category': category,
        'images': images,
        'products_picked': products_picked,
        'products_latest': products_latest,
        # 'comments': comments,
    }
    return render(request, 'product_detail.html', context)


def search(request):
    if request.method == 'POST': #Check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] #get form input data
            catid = form.cleaned_data['catid']
            if catid==0:
                products = Product.objects.filter(title__icontains=query) #SELECT *FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query, category_id=catid)

            category = Category.objects.all()
            context = {'products': products,
                       'query':query,
                       'category': category}
            return render(request, 'search.html', context)
    return HttpResponseRedirect('/')

#
# def blog(request):
#     blog = Blog.objects.all().order_by()[:4]
#     return render(request, 'blog.html', {'blog': blog})
#
#
# def blog_detail(request,id):
#     category = Category.objects.all()
#     product = Product.objects.all().order_by('?')[:8]
#     blog = Blog.objects.get(pk=id)
#
#     context = {
#         'blog': blog,
#         'category': category,
#         'product':product,
#
#     }
#     return render(request, 'blogdetail.html', context)