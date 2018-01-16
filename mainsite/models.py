#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

KIND_CHOICES = (
    ('1','科技'),
    ('2','国内'),
    ('3','国外'),
    ('4','生活'),
    ('5','资讯'),
)

class Post(models.Model):
    title = models.CharField('标题',max_length=200)
    slug = models.CharField('地址',max_length=200)
    content = models.TextField('正文',)
    kind = models.CharField('分类',max_length=20,choices=KIND_CHOICES,default=KIND_CHOICES[0])
    pub_date = models.DateTimeField('时间',default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')