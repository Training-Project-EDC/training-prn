from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style

style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'training_prn'
    verbose_name = 'Training PRN'
    admin_site_name = 'training_prn_admin'
