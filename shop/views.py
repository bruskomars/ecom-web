from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    products = Product.objects.all()

    search = request.GET.get('search')
    if search != '' and search is not None:
        products = Product.objects.filter(name__icontains=search)


    ############ PAGINATION ############
    paginator = Paginator(products, 4)  # USE OF PAGINATOR
    page = request.GET.get('page')

    products = paginator.get_page(page)

    context = {
        'products': products,
    }
    return render(request, 'shop/home.html', context)

def detail(request, pk):
    product_item = Product.objects.get(id=pk)
    context = {
        'product_item': product_item,
    }

    return render(request, 'shop/detail.html', context)