
from django.urls import path
from . import views
urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('thankyou/',views.thank_you, name='thank_you'),
   
    
]
