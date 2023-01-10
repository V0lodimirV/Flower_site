from django.urls import path
from . import views




urlpatterns = [
    path('', views.FlowerView.as_view()),
    path('<int:pk>/', views.FlowerDetail.as_view()),
]