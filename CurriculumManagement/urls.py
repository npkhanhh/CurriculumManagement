from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CurriculumManagement.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cm/', include('cm.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
