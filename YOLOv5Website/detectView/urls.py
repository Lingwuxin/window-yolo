from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video', views.stream_video, name='video'),
    path('watch', views.looking_one, name='watch')
]
