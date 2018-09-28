from django.contrib import admin
from .models import Script, Test, Host, ScriptHostMapping

modelsToRegister = [Script, Test, Host, ScriptHostMapping]
admin.site.register(modelsToRegister)
