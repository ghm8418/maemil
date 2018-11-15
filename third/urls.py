from django.contrib import admin
from django.urls import path

from app.views import index, list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('list/', list)]
