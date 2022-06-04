from django.contrib import admin
from django.urls import path
#from .import views
#from views import

from .views import Homeview, DeleteCityView

urlpatterns = [
    path('', Homeview, name='home'),
    path('delete/<str:city_name>/', DeleteCityView, name='delete'),
    ]


#from .import views
