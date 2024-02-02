from django.shortcuts import render
from .models import Product, Order
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

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        total = request.POST.get('total')

        order = Order(name=name,
                      items=items,
                      email=email,
                      address=address,
                      city=city,
                      state=state,
                      zipcode=zipcode,
                      total=total,
                      )
        order.save()

    return render(request, 'shop/checkout.html')