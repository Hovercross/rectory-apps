from django.conf.urls import include, url

urlpatterns = [
    url(r'^student/landing/$', 'courseevaluations.views.student.student_landing', name='courseevaluations_student_landing'),
    url(r'^student/survey/$', 'courseevaluations.views.student.student_survey', name='courseevaluations_student_survey'),

    url(r'^reports/$', 'courseevaluations.views.reports.index', name='courseevaluations_reports_status_index'),
    url(r'^reports/(?P<id>[0-9]+)/$', 'courseevaluations.views.reports.evaluation_set_index', name='courseevaluations_reports_status_index'),
    url(r'^reports/(?P<id>[0-9]+)/summary_by_student/$', 'courseevaluations.views.reports.by_student', name='courseevaluations_reports_by_student', kwargs={'show_evaluables': False}),
    url(r'^reports/(?P<id>[0-9]+)/detail_by_student/$', 'courseevaluations.views.reports.by_student', name='courseevaluations_reports_by_student', kwargs={'show_evaluables': True}),
    
    url(r'^reports/(?P<id>[0-9]+)/by_section/$', 'courseevaluations.views.reports.by_section', name='courseevaluations_reports_by_section'),
    
    #Results landing
    url(r'^results/(?P<evaluation_set_id>[0-9]+)/$', 'courseevaluations.views.results.index', name='courseevaluations_results_index'),
    
    #Course results
    url(r'^results/(?P<evaluation_set_id>[0-9]+)/teacher/(?P<teacher_id>[0-9]+)/$', 'courseevaluations.views.results.teacher', name='courseevaluations_course_results'),
    url(r'^results/(?P<evaluation_set_id>[0-9]+)/teacher/(?P<teacher_id>[0-9]+)/course/(?P<course_id>[0-9]+)/$', 'courseevaluations.views.results.teacher_course', name='courseevaluations_course_results'),
    url(r'^results/(?P<evaluation_set_id>[0-9]+)/section/(?P<section_id>[0-9]+)/$', 'courseevaluations.views.results.section', name='courseevaluations_course_results'),
    
    #IIP results
    url(r'^results/(?P<evaluation_set_id>[0-9]+)/iip/(?P<teacher_id>[0-9]+)/$', 'courseevaluations.views.results.iip', name='courseevaluations_iip_results'),
    
    #Dorm parent results
    url(r'^results/(?P<evaluation_set_id>[0-9]+)/dorm/(?P<dorm_id>[0-9]+)/$', 'courseevaluations.views.results.dorm_parent_dorm', name='courseevaluations_dorm_parent_results'),
    url(r'^results/(?P<evaluation_set_id>[0-9]+)/dorm/(?P<dorm_id>[0-9]+)/parent/(?P<parent_id>[0-9]+)/$', 'courseevaluations.views.results.dorm_parent_dorm_parent', name='courseevaluations_dorm_parent_results'),
    url(r'^results/(?P<evaluation_set_id>[0-9]+)/parent/(?P<parent_id>[0-9]+)/$', 'courseevaluations.views.results.dorm_parent_parent', name='courseevaluations_dorm_parent_results'),
    
    url(r'^email/send/student/$', 'courseevaluations.views.reports.send_student_email', name='courseevaluations_send_student_email'),
    url(r'^email/send/advisor_tutor_status/$', 'courseevaluations.views.reports.send_advisor_tutor_status', name='courseevaluations_send_advisor_tutor_status'),
    url(r'^email/send/section_status/$', 'courseevaluations.views.reports.send_teacher_per_section_email', name='courseevaluatons_send_teacher_per_section_email'),
]