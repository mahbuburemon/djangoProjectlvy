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
    path('', views.home, name ='home'),          # No spaces around the path string
    path('products/', views.products, name ='products'),   # No spaces around the path string
    path('customers/<str:pk_test>/', views.customers, name ='customers'), # No spaces around the path string
    path('create_order/', views.cereatOrder, name ='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name ='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name ='delete_order'),
]
