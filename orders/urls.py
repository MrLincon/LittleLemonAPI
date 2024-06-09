from django.urls import path, include

from .views import AddCartView, FetchCartItemView, ConfirmOrderView, FetchOrderView

urlpatterns = [
    path('add-to-cart/', AddCartView.as_view()),
    path('fetch-cart/<str:customer_id>', FetchCartItemView.as_view()),
    path('confirm-order/<str:customer_id>', ConfirmOrderView.as_view()),
    path('fetch-order/<str:order_id>', FetchOrderView.as_view()),
]
