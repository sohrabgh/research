from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^$','blog.views.index'),
    url(r'^add_category/','blog.views.addCategory'),
)
