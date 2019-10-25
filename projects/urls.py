from django.urls import path
from projects import views


urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
]
