from django.db import models
from django.utils.timezone import now

import uuid
from django_prose_editor.sanitized import SanitizedProseEditorField


class Page(models.Model):
    
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=255,blank=True,null=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(default=now,editable=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

class SeoMeta(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    meta_title = models.CharField(max_length=255,blank=True,null=True)
    meta_description = models.CharField(max_length=255,blank=True,null=True)
    index = models.BooleanField(default=True)
    follow = models.BooleanField(default=True)
    page = models.OneToOneField("pages.Page", verbose_name="SEO metadata", on_delete=models.CASCADE,blank=True,null=True,related_name="seo")

    def __str__(self):
        if self.meta_title:
            return 'Title:' + self.meta_title + ' - (Index:' + str(self.index) + ', Follow:' + str(self.follow) + ')'
        else:
            return 'Title:n/a' + ' - (Index:' + str(self.index) + ', Follow:' + str(self.follow) + ')'