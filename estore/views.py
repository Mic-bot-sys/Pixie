from django.db.models.lookups import EndsWith
from django.forms.fields import SlugField
from django.shortcuts import get_object_or_404, render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from .models import Item, Contactus, Subscribe
from django.contrib import messages

# Create your views here.
# class Index(TemplateView):
#     template_name = 'index.html'


class ItemLisitView(ListView):
    context_object_name = "itemm"
    model = Item
    template_name = "product.html"


class ItemDetailView(DetailView):
    context_object_name = "items"
	# specify the model to use
    model = Item
    template_name = "item_detail.html"


def index(request):
    itemm = Item.objects.all()
    return render(request, "index.html", {"itemm":itemm})

def checkout(request):
    check = Item.objects.all()
    return render(request, 'checkout.html', {"check":check})

def item_detail(request, slug):
    pick = get_object_or_404(Item, slug=slug)
    return render(request, 'item_detail.html', {"pick":pick})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def contactconf(request):
    return render(request, 'contactconf.html')

def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        user = Contactus.objects.create(name=name, email=email, subject=subject, message=message)
        user.save();
        print("New User Created")
        # messsages.info(request, "Your Message has been Submitted.")
        return render(request, "contactconf.html")
    else:
        return render(request, 'contact.html')

def subscribe(request):
    if request.method == "POST":
        email = request.POST['email']

        if Subscribe.objects.filter(email=email).exists():
            messages.info(request, "Your Email exists in our database" )
            return render(request, 'index.html')
        else:
            user = Subscribe.objects.create(email=email)
            user.save();
            print("A new user subscribed")
    return render(request, 'subscribe.html')