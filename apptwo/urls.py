from django.urls import path

from apptwo import views

urlpatterns = [
    path('', views.template, name='temp'),
    path('index/', views.index, name='index'),
    path('form/', views.form_view, name='form'),

]