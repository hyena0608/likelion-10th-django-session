from django.contrib import admin
from django.urls import path, include
from snsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #snsapp
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    
    #detail
    
    #login
]
