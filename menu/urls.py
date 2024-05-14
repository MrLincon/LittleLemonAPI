from django.urls import path, include
from .views import AddCategoryView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('add-category/', AddCategoryView.as_view())
]