from django.contrib import admin
from core.models import evento

# Register your models here.


class evento_admin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'id')


admin.site.register(evento, evento_admin)