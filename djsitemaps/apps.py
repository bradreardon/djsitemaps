from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class SiteMapsConfig(AppConfig):
    name = 'djsitemaps'
    verbose_name = _("Site Maps")
