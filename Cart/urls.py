from django.urls import path
from . import views

urlpatterns = [
    path('Cart/', views.cart_summary, name='cart-summary'),
    path('add/', views.cart_add, name='cart-add'),
    path('delete/', views.cart_delete, name='cart-delete'),
    path('historical_index/', views.historicalindex, name='historical-index'),  # Corrected trailing slash
    path('book-item/', views.book_item, name='book-item'),  # URL for booking item
    path('unbook-item/', views.unbook_item, name='unbook-item'),  # URL for unbooking item
]
