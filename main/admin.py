from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Department)
admin.site.register(models.Semester)
admin.site.register(models.Block)
