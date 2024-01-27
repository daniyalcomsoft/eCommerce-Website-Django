from django.shortcuts import render, redirect
from shoesapp.models import *
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")

def shop(request):
    type = Type.objects.all()
    size = Size.objects.all()
    condition = Condition.objects.all()
    brand = Brand.objects.all()
    shoes = Shoes.objects.all()
    deals = Deals.objects.all()[:7]
    best = BestSelling.objects.all()[:4]
    context = {
        'type': type, 'size': size, 'condition': condition, 'brand': brand, 'shoes': shoes, 'deals': deals, 'best': best
    }
    return render(request, "shop.html", context)

def deals(request):
    deal = Deals.objects.all()
    context = {
        'deal': deal
    }
    return render(request, 'deals.html', context)

def dealsdetails(request, id):
    deal = Deals.objects.get(DealID=id)
    dealimg = DealsImage.objects.filter(Deals=deal)
    sh = Shoes.objects.all()[:4]
    context = {
        'deal': deal, 'dealimg': dealimg, 'sh':sh
    }
    return render(request, 'dealsdetails.html', context)

def bestselling(request):
    best = BestSelling.objects.all()
    context = {
        'best': best
    }
    return render(request, 'bestselling.html', context)

def bestsellingdetails(request, id):
    best = BestSelling.objects.get(BestSellingID=id)
    bsimg = BSImage.objects.filter(BestSelling=best)
    sh = Shoes.objects.all()[:4]
    context = {
        'best': best, 'bsimg': bsimg, 'sh':sh
    }
    return render(request, 'bestsellingdetails.html', context)

def shoesdetails(request, id):
    shoes = Shoes.objects.get(ShoesID=id)
    shoeimg = ShoesImage.objects.filter(Shoes=shoes)
    sh = Shoes.objects.all()[:4]
    context = {
        'shoes': shoes, 'shoeimg': shoeimg, 'sh':sh
    }
    return render(request, 'shoesdetails.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        telephone = request.POST.get('Telephone')
        email = request.POST.get('Email')
        address = request.POST.get('Address')
        message = request.POST.get('Message')

        contact = ContactUs(Name=name, Telephone=telephone, Email=email, Address=address, Message=message)
        contact.save()

        messages.success(request, 'Your message has been submitted successfully')
        return redirect('contact')

    return render(request, "contact.html")

def query(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        telephone = request.POST.get('Telephone')
        email = request.POST.get('Email')
        address = request.POST.get('Address')
        image = request.FILES.get('Image')
        message = request.POST.get('Message')

        contact = Query(Name=name, Telephone=telephone, Email=email, Address=address, Image=image, Message=message)
        contact.save()

        messages.success(request, 'Your query has been submitted successfully')
        return redirect('query')

    return render(request, "query.html")

def allshoes(request):
    shoes = Shoes.objects.all()
    context = {
        'shoes': shoes
    }
    return render(request, 'allshoes.html', context)

def shoessort(request, id):
    type = Type.objects.get(TypeID=id)
    shoes = Shoes.objects.filter(Type=type)

    context = {
        'type': type, 'shoes': shoes,
    }
    return render(request, 'shoessort.html', context)

def shoessize(request, id):
    size = Size.objects.get(SizeID=id)
    shoes = Shoes.objects.filter(Size=size)
    context = {
        'size':size, 'shoes': shoes
    }
    return render(request, 'shoessize.html', context)

def shoescondition(request, id):
    condition = Condition.objects.get(ConditionID=id)
    shoes = Shoes.objects.filter(Condition=condition)
    context = {
        'condition': condition, 'shoes': shoes
    }
    return render(request, 'shoescondition.html', context)


# def shoessort(request, id):
#     try:
#         type = Type.objects.get(TypeID=id)
#         shoes = Shoes.objects.filter(Type=type)
#         context = {'type': type, 'shoes': shoes}
#     except Type.DoesNotExist:
#         try:
#             size = Size.objects.get(SizeID=id)
#             shoes = Shoes.objects.filter(Size=size)
#             context = {'size': size, 'shoes': shoes}
#         except Size.DoesNotExist:
#             # Handle the case when neither Type nor Size is found for the given id
#             context = {'error_message': f"No matching Type or Size found for ID: {id}"}

#     return render(request, 'shoessort.html', context)

def shoesprice(request):
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', float('inf'))

    type_filter = request.GET.get('type', '')

    shoes = Shoes.objects.filter(Price__gte=min_price, Price__lte=max_price)

    if type_filter:  # If a shoe type filter is specified, filter by that type
        shoes = shoes.filter(Type__Name=type_filter)
        
    context = {
        'shoes': shoes
    }
    return render(request, 'shoesprice.html', context)

def videos(request):
    videos = Videos.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'videos.html', context)

def shoesreviews(request):
    shreviews = ShoesReviews.objects.all()
    context = {
        'shreviews': shreviews
    }
    return render(request, 'shoesreviews.html', context)

def gallery(reuqest):
    gallery = Gallery.objects.all()
    context = {
        'gallery': gallery
    }
    return render(reuqest, 'gallery.html', context)

def returnpolicy(request):
    return render(request, 'returnpolicy.html' )