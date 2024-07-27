from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    models = Post
    queryset = Post.objects.order_by('time_in')
    template_name = 'news.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    models = Post
    template_name = 'news_id.html'
    context_object_name = 'news'

    def get_queryset(self):
        return Post.objects.all()