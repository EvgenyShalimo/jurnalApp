from django.contrib import admin
from .models import Person
from django.utils.html import format_html

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')




admin.site.register(Person, PersonAdmin)