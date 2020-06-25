from django.conf.urls import re_path

from djsitemaps.tests.urls.http import SimpleSitemap


class HTTPSSitemap(SimpleSitemap):
    protocol = 'https'

secure_sitemaps = {
    'simple': HTTPSSitemap,
}

urlpatterns = [
    (r'^secure/index\.xml$', 'djsitemaps.views.index', {'sitemaps': secure_sitemaps}),
    (r'^secure/sitemap-(?P<section>.+)\.xml$', 'djsitemaps.views.sitemap',
        {'sitemaps': secure_sitemaps}),
]
