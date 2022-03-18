from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index),
    path('result', views.process_money),
]

urlpatterns += staticfiles_urlpatterns()