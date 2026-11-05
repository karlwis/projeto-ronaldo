from django.contrib import admin
from django.urls import path
from myauth.views import home, health

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('health/', health, name='health'),
]
