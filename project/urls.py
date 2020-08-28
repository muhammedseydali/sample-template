from django.urls import path 
from project import views

urlpatterns = [
    path('indexx/',views.index, ),
    path('ali/',views.ali),
    path('contact/',views.contact),
    path('destinations/',views.destinations),
    path('elements/',views.elements),
  	path('news/',views.news),
]