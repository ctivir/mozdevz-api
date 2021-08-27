from django.contrib import admin
from .models import Program, Geral, Contact, Person


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'img_url')

class EmbassadorAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'img_url')

class GeralAdmin(admin.ModelAdmin):
    list_display = ('description', 'logo')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'message')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'team', 'ocupation', 'img_url')


# Register your models here.
admin.site.register(Program, ProgramAdmin)
admin.site.register(Geral, GeralAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Person, PersonAdmin)
