from django.contrib import admin
from notes.models import Note, Tag, SeoMeta
from django.contrib.admin.options import TabularInline
from notes.forms import TagFormAdmin



class SeoMetaInline(admin.TabularInline):
    model = SeoMeta
    can_delete = True
    verbose_name_plural = 'SEO Settings'


class NoteAdmin(admin.ModelAdmin):
    inlines = [SeoMetaInline]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'status', 'updated_date','created_date','seo')
    search_fields = ('title', 'content')


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    form = TagFormAdmin

admin.site.register(Tag, TagAdmin)
admin.site.register(Note, NoteAdmin)


