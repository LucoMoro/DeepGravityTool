from django.urls import path
from . import views

urlpatterns=[
    path('', views.tool, name='home'),
    path('dg_results', views.dg_results, name='dg_results'),
    path('g_results', views.g_results, name='g_results'),
    path('ng_results', views.ng_results, name='ng_results'),
    path('mfg_results', views.mfg_results, name='mfg_results'),
    path('jupyter', views.jupyter, name='jupyter'),
    path('navtest', views.navtest, name='navtest'),
    path('about_me', views.about_me, name='about_me'),
    path('footertest', views.footertest, name='footertest'),
]