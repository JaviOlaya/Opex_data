from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page,PageAdmin)

title = "Django's project"
subtitle = "Management panel"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle