from django.urls import path
from . import views


app_name = "quotes" 

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('author/<str:author_id>/',  views.author, name="author_info"),
    path('tag/<str:tag>/',  views.tag_search, name="tag"),
    path('create/author/',  views.create_author, name="create_author"),
    path('create/quote/',  views.create_quote, name="create_quote"),
    path('create/tag/',  views.create_tag, name="create_tag"),
]