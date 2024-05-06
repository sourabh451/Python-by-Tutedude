from django.urls import include, re_path
from django.contrib import admin
from . import views
urlpatterns = [
    re_path(r'^$',views.IndexView.as_view(),name='index'),
    re_path(r'^edit/(?P<pk>[0-9]+)$', views.StudentUpdate.as_view(),name='student_edit'),
]