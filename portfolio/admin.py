from portfolio.models import Contact, Blog, Work
from django.contrib import admin

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", 'location', "email", 'message')


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Contact, ContactAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Work, WorkAdmin)
