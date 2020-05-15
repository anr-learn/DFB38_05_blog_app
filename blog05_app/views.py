# DFB38_05_blog_app/blog05_app/views.py

#from django.shortcuts import render
from django.views.generic import ListView

from .models import BlogPost


class BlogListView(ListView):
	""" """

	model = BlogPost

	template_name = "home.html"


### end ###
