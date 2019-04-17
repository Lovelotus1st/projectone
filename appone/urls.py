from django.urls import path

from . import views

urlpatterns = [
    path('',views.template, name ='template'),
    path('index/', views.index, name='index'),
    path('form/', views.form_view, name='form'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
