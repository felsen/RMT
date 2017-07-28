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

    url(r'^resume-management/view/(?P<res_id>\d+)/$',
        rmt_views.view_resume_mgmt, name='view-resume-management'),

    url(r'^requirement-management/$', rmt_views.requirement_mgmt,
        name='requirement-management'),

    url(r'^requirement-management/add/$', rmt_views.add_requirement_mgmt,
        name='add-requirement-mgmt'),

    url(r'^requirement-management/edit/(?P<req_id>\d+)/$',
        rmt_views.edit_requirement_mgmt, name='edit-requirement-mgmt'),

    url(r'^requirement-management/view/(?P<req_id>\d+)/$',
        rmt_views.view_requirement_mgmt, name='requirement-mgmt-view'),

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

    url(r'^update-role/$', rmt_views.update_role, name='update-role'),

    url(r'^is-status/(?P<resume_id>\d+)/(?P<req_id>\d+)/$',
        rmt_views.update_resume_status, name='update-resume-status'),

    url(r'^update-interview-schedule/(?P<scheduled_id>\d+)/(?P<req_id>\d+)/$',
        rmt_views.update_schedule, name='interview-schedule'),

    url(r'^interview-history/(?P<resume_id>\d+)/(?P<req_id>\d+)/$',
        rmt_views.interview_history, name='interview-history'),

    url(r'^update-approval-status/$',
        rmt_views.update_approval_status, name='update-approval-status'),

    url(r'^generate-col-letter/(?P<hrmgmt_id>\d+)/$',
        rmt_views.generate_col_letter, name='generate-col-letter'),

    url(r'^update-salary-details/(?P<hrmgmt_id>\d+)/$',
        rmt_views.update_salary_details, name='update-salary-details'),

    url(r'^reports/$', rmt_views.reports, name='reports'),

    url(r'^reports/(?P<status>\w+)/$', rmt_views.reports,
        name='report-status'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
