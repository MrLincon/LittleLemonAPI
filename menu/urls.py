from django.urls import path, include
from .views import AddCategoryView, UpdateCategoryView, DeleteCategoryView, FetchCategoriesView
from .views import AddItemView, UpdateItemView, DeleteItemView, FetchItemsView, FetchItemsByCategoryView, FeatureItemView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('categories/all', FetchCategoriesView.as_view()),
    path('add-category/', AddCategoryView.as_view()),
    path('update-category/<str:category_id>', UpdateCategoryView.as_view()),
    path('delete-category/<str:category_id>', DeleteCategoryView.as_view()),

    path('items/all', FetchItemsView.as_view()),
    path('add-item/', AddItemView.as_view()),
    path('update-item/<str:item_id>', UpdateItemView.as_view()),
    path('delete-item/<str:item_id>', DeleteItemView.as_view()),
    path('items/<str:category_id>', FetchItemsByCategoryView.as_view()),
    path('items-feature/<str:item_id>', FeatureItemView.as_view()),
]
