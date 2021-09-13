from django.urls import path

from accounting import views

urlpatterns = [
    path('companies/', views.CompanyList.as_view()),
    path('companies/<int:pk>/', views.CompanyDetail.as_view()),
]
