from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('register/', views.register_req, name='register'),
    path('login/', views.login_req, name='login'),
    path('logout/', views.logout_req, name='logout'),
    path('suggest/', views.suggest_location, name='suggest'),
    path('suggest/new', views.suggest_new_location, name='suggest-new'),
    #path('about/', AboutPageView.as_view(), name='about')
]