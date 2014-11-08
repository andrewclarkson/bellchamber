from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'products.views.index'),
    url(r'^/(?P<category>[\w-]+)', include([
        url(r'^$', 'products.views.category'),
        url(r'^/(?P<page>[0-9]+)$', 'products.views.category'),
        url(r'^/(?P<product>[\w-]+)$', 'products.views.show'),
    ])),
)
