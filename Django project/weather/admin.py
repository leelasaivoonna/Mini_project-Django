from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.urls import path
from weather.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
]