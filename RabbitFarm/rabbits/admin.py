# rabbits/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Rabbit

class RabbitAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'image_display')

    def image_display(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "No Image"

    image_display.short_description = 'Image'

admin.site.register(Rabbit, RabbitAdmin)
