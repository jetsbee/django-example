from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUseradmin(admin.ModelAdmin):
    pass
