from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('about/', views.menu_pages, name='about'),
    path('team', views.menu_pages, name='team'),
    path('contact', views.menu_pages, name='contact'),
    path('mobile-apps/', views.menu_pages, name='mobile_apps'),
    path('blog/', views.menu_pages, name='blog'),
    path('web-development/', views.menu_pages, name='web_development'),
    path('flask/', views.menu_pages, name='flask'),
    path('django/', views.menu_pages, name='django'),
    path('fastapi/', views.menu_pages, name='fastapi')
]
