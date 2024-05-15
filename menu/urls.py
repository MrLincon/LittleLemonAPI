from django.urls import path, include
from .views import AddCategoryView, UpdateCategoryView, FetchCategoriesView, AddItemView, UpdateItemView, FetchItemsView, FetchItemsByCategoryView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('add-category/', AddCategoryView.as_view()),
    path('update-category/<str:category_uid>', UpdateCategoryView.as_view()),
    path('categories/all', FetchCategoriesView.as_view()),
    path('add-item/', AddItemView.as_view()),
    path('update-item/<str:item_uid>', UpdateItemView.as_view()),
    path('items/all', FetchItemsView.as_view()),
    path('items/<str:category_uid>', FetchItemsByCategoryView.as_view()),
]
