from django import views
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
app_name = 'rest'
urlpatterns = [
    path('', home, name="home"),
    path('plats/', plats, name="plats"),
    path('ambiance/', ambiance, name="ambiance"),
    path('<int:pk>', detail, name="detail"),
    path('<int:pk>/dl', detail_d, name="detail_d"),
] 
