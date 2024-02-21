
from django.contrib import admin
from django.urls import path
from hostelapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage' ),
    path('aboutus/',views.about,name='about'),
    path('form/',views.form,name='form'),



]
