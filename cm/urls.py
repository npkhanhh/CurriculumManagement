from django.conf.urls import patterns, url
import cm.views as v

urlpatterns = patterns('',
    url(r'^add_program/$', v.add_program, name='add_program'),
    url(r'^import_subject/$', v.import_subject,name='import_subject'),
    url(r'^login/$', v.login, name='login'),
    url(r'^bok/(?P<bok_id>\d+)/$', v.bok_detail, name='bok_detail'),
    url(r'^subject/(?P<subject_id>.+)/$', v.subject_detail, name='subject_detail'),
    url(r'^(?P<program_id>.+)/(?P<major_id>\d+)/$', v.major_detail, name='major_detail'),
    url(r'^(?P<program_id>.+)/$', v.program_detail, name='program_detail'),
    url(r'^$', v.view_programs, name='view_programs'),
)