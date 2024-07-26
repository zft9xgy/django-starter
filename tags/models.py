from django.db import models
import uuid
from django.db.models import Count, Q


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


    @staticmethod
    def get_tags(number_of_tags : int = None) -> list:
        """
        Devuelve una lista de tags donde cada tag tiene al menos un post publicado. Exclude tags con 0 post.
        La lista de tags se ofrece ordenado por cantidad de post.
        Si se da un numero, este será el número máximo de tags que se devuelvan.

        """
        #tags = Tag.objects.annotate(note_count=Count('notes')).filter(Q(note_count__gt=0)).order_by('-note_count')

        tags = (
            Tag.objects.annotate(
                published_note_count=Count('notes', filter=Q(notes__status='published'))
            )
            .filter(published_note_count__gt=0)
            .order_by('-published_note_count')
        )


        if number_of_tags:
            return tags[:number_of_tags]
        
        return tags
    
    def __str__(self):
        return self.name

