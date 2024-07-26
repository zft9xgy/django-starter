from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
import uuid
from django_prose_editor.sanitized import SanitizedProseEditorField
from filer.fields.image import FilerImageField
from django.db.models import Count, Q


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    @staticmethod
    def get_tags(number_of_tags : int = None) -> list:
        """
        Devuelve una lista de etiquetas (tags) que tengan Notas asociadas a ellas. 
        Por defecto, devuelve todas las etiquetas disponibles que tenga al menos una Nota.

        Args:
        number_of_tags (int): El número de etiquetas a devolver.

        Returns:
        list: Una lista de etiquetas.
        """
        tags = Tag.objects.annotate(note_count=Count('notes')).filter(Q(note_count__gt=0)).order_by('-note_count')
        if number_of_tags:
            return tags[:number_of_tags]
        return tags
    
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