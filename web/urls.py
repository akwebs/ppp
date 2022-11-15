from django.urls import path

from .views import *

app_name = 'web'

urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:slug>/', blog_category, name='blog_category'),
    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', blogdetails, name='blogdetails'),
    path('projects/', projects, name='projects'),
    path('projects/<slug:slug>/', projectdetails, name='projectdetails'),
    path('connect/', contact, name='contact'),
]
