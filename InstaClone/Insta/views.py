from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.views.generic import ListView, CreateView


# Create your views here.


class PostListView(ListView):
    template_name = "insta/post_list.html"
    queryset = Post.objects.all()
    context_object_name = "posts"


class PostCreateView(CreateView):
    template_name = "insta/post_create.html"
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
