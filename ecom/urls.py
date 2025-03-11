from django.contrib import admin
from django.urls import path,include
from ecom import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
]

