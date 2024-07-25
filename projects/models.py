from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import URLValidator



class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True,null=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True,validators=[URLValidator()])
    source_link = models.CharField(max_length=2000, null=True, blank=True,validators=[URLValidator()])
    note_link = models.CharField(max_length=2000, null=True, blank=True,validators=[URLValidator()])

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
