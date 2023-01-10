from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsView.as_view()),
    path('<int:pk>/', views.NewsDetail.as_view()),
    path('about/', views.AboutUs.as_view()),
]