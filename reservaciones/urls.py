from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [


    url(r'^pago/$', 'app.views.pick_up', name='pick_up'),



]
