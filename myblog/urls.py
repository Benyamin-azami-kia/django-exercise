from unicodedata import name
from django.urls import path

from . import views

urlpatterns=[
    path('', views.HomePageView.as_view(), name='index'),
    path('posts/', views.PostsView.as_view(), name="posts"),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('read_later', views.ReadLaterView.as_view(), name='read_later')
]