from django.urls import path
from .views import (
    post_list,
    post_detail
)

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post-list'),
    path('/<slug>/', post_detail, name='post'),
]
