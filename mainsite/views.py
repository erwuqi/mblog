#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime

# Create your views here.
def index(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    #post_lists = list()
    #for count,post in enumerate(posts,1):
    #    post_lists.append("No.{}:".format(str(count)) + str(post) + "<br />")
    #    post_lists.append("<small>" + str(post.content) + "</small><br />")
    return HttpResponse(html)

def showpost(request,slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
