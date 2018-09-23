# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding("utf8")

from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author','views']
 

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
