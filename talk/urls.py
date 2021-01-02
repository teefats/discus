from django.urls import path
from . import views
from django.contrib import admin

# from discus import talk

app_name ='talk'

urlpatterns = [
    path('', views.main_view, name ='main_view'),
    path('addInForum/',views.addInForum,name='addInForum'),
    path('addInDiscussion/', views.addInDiscussion,name='addInDiscussion'),

]
