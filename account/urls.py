# from django.urls import path
# from.import views

# urlpatterns = [
#     path(' ', views.home),
#     path('products/ ', views.products),
#     path(' customers/ ', views.customers),
  
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),          # No spaces around the path string
    path('products/', views.products),   # No spaces around the path string
    path('customers/', views.customers), # No spaces around the path string
]
