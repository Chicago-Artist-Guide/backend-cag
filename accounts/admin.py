from django.contrib import admin
from django.apps import apps


for app_config in apps.get_app_configs():
    for model in app_config.get_models():
        if admin.site.is_registered(model):
            pass
        else:
            admin.site.register(model)
