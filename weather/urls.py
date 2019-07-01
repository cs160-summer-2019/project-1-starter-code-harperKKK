from django.urls import path

from . import views

urlpatterns = [
    path('forecast/', views.forecast, name='forecast'),
    path('forecast/alert/', views.forecast_alert, name='forecast_alert'),
    path('comparison/', views.comparison, name='comparison'),
    path('map/', views.map, name='map'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]