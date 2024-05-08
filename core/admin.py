from django.contrib import admin
from .models import Games
# Register your models here.
@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','link',)
    search_fields   = ('id', 'name')
