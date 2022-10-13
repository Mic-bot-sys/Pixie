"""mic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'estore'

urlpatterns = [
    # path('', views.Index.as_view(), name='index'),
    path('', views.index, name='index'),
    # path('product/', views.product, name='product'),
    path('product/', views.ItemLisitView.as_view(), name='product'),
    path('contact/', views.contact, name='contact'),
    path('contactconf/', views.contactconf, name="contactconf"),
    path('contactus/', views.contactus, name='contactus'),
    path('about/', views.about, name='about'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('checkout/', views.checkout, name='checkout'),
    path('admin/', admin.site.urls),
    path('product/<slug:slug>/', views.item_detail, name="description"),    
    # path('product/<slug:slug>', views.ItemDetailView.as_view(), name="description"),
    # path('product/<slug:slug>/', views.item_detail, name ="ite"),
]
