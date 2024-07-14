from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [

    path('', views.BooksView.as_view(), name="books"),
    path('books/<pk>/', views.BookDetailView.as_view(), name="book_detail"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.show_about, name='about'),

]
