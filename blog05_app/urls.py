# DFB38_05_blog_app/blog05_app/urls.py

from django.urls import path

from .views import BlogListView

urlpatterns = [
	path("", BlogListView.as_view(), name="home"),
	]

### end ###
