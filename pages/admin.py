from django.contrib import admin
from pages.models import Page, SeoMeta
from django.contrib.admin.options import TabularInline



class SeoMetaInline(admin.TabularInline):
    model = SeoMeta
    can_delete = True
    verbose_name_plural = 'SEO Settings'

class PageAdmin(admin.ModelAdmin):
    inlines = [SeoMetaInline]
    list_display = ('title', 'created_date', 'updated_date','seo')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Page, PageAdmin)

