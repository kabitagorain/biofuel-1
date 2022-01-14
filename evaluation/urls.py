from django.urls import path
from . import views

app_name = 'evaluation'
urlpatterns = [
    path('', views.index, name='index'),    
    path('option_add/', views.option_add, name='option_add'),  
    path('option_append/', views.option_append, name='option_append'),
    path('report/', views.report, name='report'),         
    
    
]