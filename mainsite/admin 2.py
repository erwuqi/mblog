#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Post,PostAdmin

# Register your models here.

admin.site.register(Post,PostAdmin)