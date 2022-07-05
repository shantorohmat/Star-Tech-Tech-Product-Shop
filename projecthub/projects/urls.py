from typing import ValuesView
from django.urls import path
from django.urls import path
from .import views 

urlpatterns = [
    path('projects/',views.projects,name="projects"),
    path('projects/create-project/',
        views.create_project,name="create_project"),
    path('projects/<str:project_id>/',
        views.project_detail, name="project_detail"), 
    path('projects/update-project/<str:project_id>/',
        views.edit_project, name="edit_project"),  
    path('projects/delete-project/<str:project_id>/', views.delete_project,name="delete_project" ),
    
    path("register/", views.register_request, name="register"), # new

    path("login/", views.login_request, name="login"),

    path('',views.home,name='home'),
    path("logout", views.logout_request, name= "logout"),
   
   
   
    path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
]
