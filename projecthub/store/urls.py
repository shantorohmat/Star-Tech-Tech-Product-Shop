
from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('projects/store/', views.store, name="store"),
	path('projects/cart/', views.cart, name="cart"),
	path('projects/checkout/', views.checkout, name="checkout"),

]