from django.contrib import admin
from notes.models import Note, SeoMeta
from django.contrib.admin.options import TabularInline



class SeoMetaInline(admin.TabularInline):
    model = SeoMeta
    can_delete = True
    verbose_name_plural = 'SEO Settings'


class NoteAdmin(admin.ModelAdmin):
    inlines = [SeoMetaInline]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'status', 'updated_date','created_date','seo')
    search_fields = ('title', 'content')

admin.site.register(Note, NoteAdmin)


