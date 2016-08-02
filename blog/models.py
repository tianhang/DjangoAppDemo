from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add= True)
    modified = models.DateTimeField(auto_now= True)
    class Meta:
        abstract = True

class BlogPost(TimeStampModel):
    title = models.CharField(max_length=150)
    body = models.TextField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','modified')

admin.site.register(BlogPost,BlogPostAdmin)


