from django.urls import path, include
from projects import views


urlpatterns = [
    # path('', views.home_index, name='home_index'),
    path('id<int:pk>/', views.home_page, name='home_page'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('', views.signout, name='signout'),
    path('checkemail/', views.activation_sent, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate_user, name='activate'),
]
