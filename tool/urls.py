from django.urls import path
from . import views

urlpatterns=[
    path('', views.tool, name='home'),
    path('results', views.results, name='results'),
    path('jupyter', views.jupyter, name='jupyter'),
    path('navtest', views.navtest, name='navtest'),
    path('footertest', views.footertest, name='footertest'),
]