from notes.models import Note
from pages.models import Page
from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.urls import reverse
from django.db.models import Q


class NotesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
    # Obtener todas las notas publicadas con seo.index = True o sin relación SeoMeta
        notes = Note.objects.filter(
            Q(status='published') & 
            (Q(seo__index=True) | Q(seo=None))
            )
        return notes

    def location(self, item):
        return reverse('note',args=[item.slug])

    def lastmod(self, obj):
        return obj.updated_date

class PagesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        pages = Page.objects.filter(
            (Q(seo__index=True) | Q(seo=None))
        )
        return pages

    def location(self, item):
        return reverse('page',args=[item.slug])

    def lastmod(self, obj):
        return obj.updated_date


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = "daily"

    def items(self):
        return ["home", "projects", "tags","notes"]

    def location(self, item):
        return reverse(item)


sitemaps = {
    'statics': StaticViewSitemap,
    'notes': NotesSitemap,
    'pages': PagesSitemap,
}