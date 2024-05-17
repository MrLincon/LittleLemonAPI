from django.urls import path, include

from .views import AddOrderView

urlpatterns = [
    path('add-order/', AddOrderView.as_view()),
]
