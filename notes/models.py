from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
import uuid
from django_prose_editor.sanitized import SanitizedProseEditorField
from filer.fields.image import FilerImageField


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class Note(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    excerpt = models.CharField(max_length=255,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    featured_image = FilerImageField(null=True, blank=True,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='notes',blank=True)
    created_date = models.DateTimeField(default=now,editable=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return "(" + self.status + ") " + self.title




class SeoMeta(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    meta_title = models.CharField(max_length=255,blank=True,null=True)
    meta_description = models.CharField(max_length=255,blank=True,null=True)
    index = models.BooleanField(default=True)
    follow = models.BooleanField(default=True)
    note = models.OneToOneField("notes.Note", verbose_name="SEO metadata", on_delete=models.CASCADE,blank=True,null=True,related_name="seo")

    def __str__(self):
        if self.meta_title:
            return 'Title:' + self.meta_title + ' - (Index:' + str(self.index) + ', Follow:' + str(self.follow) + ')'
        else:
            return 'Title:n/a' + ' - (Index:' + str(self.index) + ', Follow:' + str(self.follow) + ')'