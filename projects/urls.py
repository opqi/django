from django.urls import path
from projects import views


urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('<int:pk>/', views.home_index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('checkemail/', views.activation_sent, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate_user, name='activate'),
]
