from django.conf.urls import patterns

from djsitemaps.tests.urls.http import SimpleSitemap


class HTTPSSitemap(SimpleSitemap):
    protocol = 'https'

secure_sitemaps = {
    'simple': HTTPSSitemap,
}

urlpatterns = patterns('djsitemaps.views',
    (r'^secure/index\.xml$', 'index', {'sitemaps': secure_sitemaps}),
    (r'^secure/sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': secure_sitemaps}),
)
