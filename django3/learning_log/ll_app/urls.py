""" urls.py for ll_app """

from django.urls import path
from . import views

app_name = 'll_app'

urlpatterns = [
    # Home page for ll_app
    path('', views.index, name = 'index'),
]
