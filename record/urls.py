from django.urls import path
from . import views

urlpatterns = [
    #home page  
    path('', views.home, name='home'),
    #logout page
    path('logout/', views.logout_user, name='logout'),
    #regitration page   
    path('register/', views.register_user, name='register'),
    #reord page 
    path('record/<int:pk>', views.patient_record, name='record'),
    #deletion of record
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    #add record page    
    path('add/', views.add_record, name='add_record'),
    #edit record page   
    path('edit/<int:pk>/', views.edit_record, name='edit_record'),
]



