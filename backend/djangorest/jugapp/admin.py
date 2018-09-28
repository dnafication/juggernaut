from django.contrib import admin
from .models import Script, Test, Host, Mapping

modelsToRegister = [Script, Test, Host, Mapping]
admin.site.register(modelsToRegister)
