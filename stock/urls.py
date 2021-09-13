from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from stock import views

urlpatterns = [
    path('items/', views.item_list),
    path('warehouses/', views.WarehouseList.as_view()),
    path('warehouses/<int:pk>/', views.WarehouseDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
