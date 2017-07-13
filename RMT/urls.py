from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rolemgmt import views as role_views
from rmtmgmt import views as rmt_views
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^user-login/$', role_views.user_login, name='user-login'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/user-login/'}),

    url(r'^$', rmt_views.resume_mgmt,
        name='resume-management'),

    url(r'^resume-management/$', rmt_views.resume_mgmt,
        name='resume-management'),

    url(r'^resume-management/add/$', rmt_views.add_resume_mgmt,
        name='add-resume-management'),

    url(r'^resume-management/edit/(?P<res_id>\d+)/$',
        rmt_views.edit_resume_mgmt, name='edit-resume-management'),

    url(r'^requirement-management/$', rmt_views.requirement_mgmt,
        name='requirement-management'),

    url(r'^requirement-management/add/$', rmt_views.add_requirement_mgmt,
        name='add-requirement-mgmt'),

    url(r'^requirement-management/edit/(?P<req_id>\d+)/$',
        rmt_views.edit_requirement_mgmt, name='edit-requirement-mgmt'),

    url(r'^client-management/add/$', rmt_views.add_client_mgmt,
        name='add-client-mgmt'),

    url(r'^client-management/edit/(?P<client_id>\d+)/$',
        rmt_views.edit_client_mgmt, name='edit-client-mgmt'),

    url(r'^client-management/status/(?P<client_id>\d+)/$',
        rmt_views.status_client_mgmt, name='status-client-mgmt'),

    url(r'^client-management/$', rmt_views.client_mgmt,
        name='client-management'),

    url(r'^hr-management/$',
        rmt_views.hr_mgmt, name='hr-management'),

    url(r'^role-management/$',
        rmt_views.role_management, name='role-management'),

    url(r'^role-management/(?P<status>(:?inactive|:?active))/$',
        rmt_views.role_management, name='role-management'),

    url(r'^role-management/(?P<status>(:?deactivate|:?activate))/(?P<user_id>\d+)/$',
        rmt_views.role_management_status, name='role-management'),

    url(r'^interview-schedule/$', rmt_views.interview_schedule,
        name='interview-schedule'),

    url(r'^user-registration/$', role_views.user_registration,
        name='user-registration'),

    url(r'^approvals/$', rmt_views.approvals, name='approvals'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
