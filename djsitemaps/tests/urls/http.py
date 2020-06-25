from datetime import date, datetime
from django.conf.urls import patterns, re_path
from djsitemaps import Sitemap, GenericSitemap, FlatPageSitemap, views
from django.utils import timezone
from django.views.decorators.cache import cache_page

from django.contrib.sitemaps.tests.base import TestModel


class SimpleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    location = '/location/'
    lastmod = datetime.now()

    def items(self):
        return [object()]


class EmptySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    location = '/location/'

    def items(self):
        return []


class FixedLastmodSitemap(SimpleSitemap):
    lastmod = datetime(2013, 3, 13, 10, 0, 0)


class FixedLastmodMixedSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    location = '/location/'
    loop = 0

    def items(self):
        o1 = TestModel()
        o1.lastmod = datetime(2013, 3, 13, 10, 0, 0)
        o2 = TestModel()
        return [o1, o2]


class DateSiteMap(SimpleSitemap):
    lastmod = date(2013, 3, 13)


class TimezoneSiteMap(SimpleSitemap):
    lastmod = datetime(2013, 3, 13, 10, 0, 0, tzinfo=timezone.get_fixed_timezone(-300))


simple_sitemaps = {
    'simple': SimpleSitemap,
}

empty_sitemaps = {
    'empty': EmptySitemap,
}

fixed_lastmod_sitemaps = {
    'fixed-lastmod': FixedLastmodSitemap,
}

fixed_lastmod__mixed_sitemaps = {
    'fixed-lastmod-mixed': FixedLastmodMixedSitemap,
}

generic_sitemaps = {
    'generic': GenericSitemap({'queryset': TestModel.objects.all()}),
}

flatpage_sitemaps = {
    'flatpages': FlatPageSitemap,
}

urlpatterns = [
    re_path(r'^simple/index\.xml$', 'djsitemaps.views.index', {'sitemaps': simple_sitemaps}),
    re_path(r'^simple/custom-index\.xml$', 'djsitemaps.views.index',
        {'sitemaps': simple_sitemaps, 'template_name': 'custom_sitemap_index.xml'}),
    re_path(r'^simple/sitemap-(?P<section>.+)\.xml$', 'djsitemaps.views.sitemap',
        {'sitemaps': simple_sitemaps}),
    re_path(r'^simple/sitemap\.xml$', 'djsitemaps.views.sitemap', {'sitemaps': simple_sitemaps}),
    re_path(r'^simple/custom-sitemap\.xml$', 'djsitemaps.views.sitemap',
        {'sitemaps': simple_sitemaps, 'template_name': 'custom_sitemap.xml'}),
    re_path(r'^empty/sitemap\.xml$', 'djsitemaps.views.sitemap', {'sitemaps': empty_sitemaps}),
    re_path(r'^lastmod/sitemap\.xml$', 'djsitemaps.views.sitemap', {'sitemaps': fixed_lastmod_sitemaps}),
    re_path(r'^lastmod-mixed/sitemap\.xml$', 'djsitemaps.views.sitemap', {'sitemaps': fixed_lastmod__mixed_sitemaps}),
    re_path(r'^lastmod/date-sitemap.xml$', views.sitemap,
        {'sitemaps': {'date-sitemap': DateSiteMap}}),
    re_path(r'^lastmod/tz-sitemap.xml$', views.sitemap,
        {'sitemaps': {'tz-sitemap': TimezoneSiteMap}}),
    re_path(r'^generic/sitemap\.xml$', 'djsitemaps.views.sitemap', {'sitemaps': generic_sitemaps}),
    re_path(r'^flatpages/sitemap\.xml$', 'djsitemaps.views.sitemap', {'sitemaps': flatpage_sitemaps}),
    re_path(r'^cached/index\.xml$', cache_page(1)(views.index),
        {'sitemaps': simple_sitemaps, 'sitemap_url_name': 'cached_sitemap'}),
    re_path(r'^cached/sitemap-(?P<section>.+)\.xml', cache_page(1)(views.sitemap),
        {'sitemaps': simple_sitemaps}, name='cached_sitemap')
]
