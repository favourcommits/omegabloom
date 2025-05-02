from django.urls import path
from omegaapp import views

urlpatterns = [
    path('', views.index, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.about, name='gallery'),
    path('index/', views.gallery, name='index'),

]