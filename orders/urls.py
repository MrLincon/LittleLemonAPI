from django.urls import path, include

from .views import AddCartView, FetchCartItemView

urlpatterns = [
    path('add-cart/', AddCartView.as_view()),
    path('fetch-cart/', FetchCartItemView.as_view()),
]
