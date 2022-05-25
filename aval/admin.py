from django.contrib import admin
from .models import Avaliation

class AvaliationModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_posted')
    date_hierarchy = 'date_posted'
    # search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')

admin.site.register(Avaliation, AvaliationModelAdmin)