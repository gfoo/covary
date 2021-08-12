from django.contrib import admin
from django.db import models
from django.forms import TextInput

from .models import Probe


class ProbeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }


admin.site.register(Probe, ProbeAdmin)
