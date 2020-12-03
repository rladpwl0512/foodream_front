from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:form_id>/', views.add_cart, name='add_cart' ),
    path('cart/', views.cart_detail, name='cart_detail'),
]