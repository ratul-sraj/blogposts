from typing import List, Dict

from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)


# Create your views here.

def home(req):
    context = {"posts": Post.objects.all()}
    return render(req, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(req):
    return render(req, "blog/about.html", {"title": "About"})
