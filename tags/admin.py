from django.contrib import admin
from notes.models import Tag



class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Tag, TagAdmin)