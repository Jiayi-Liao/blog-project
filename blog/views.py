# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from models import Post
from markdown import markdown


# Create your views here.



def index(request):
    latest_post_list = Post.objects.order_by('date').exclude(title='about')
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.body = markdown(post.body)
    context = {'post': post}
    return render(request, 'blog/post.html', context)


def about(request):
    post = get_object_or_404(Post, title='about')
    post.body = markdown(post.body)
    context = {'post': post}
    return render(request, 'blog/about.html', context)
