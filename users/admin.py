from django.contrib import admin
from .models import Profile, UserComplete


class UserCompleteModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'cpf', 'cargo', 'phone')

admin.site.register(Profile)
admin.site.register(UserComplete, UserCompleteModelAdmin)