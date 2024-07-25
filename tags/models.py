from django.db import models
import uuid

# Create your models here.

class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

