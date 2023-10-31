
from django.contrib import admin
from django.urls import path
from app1.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)

]
