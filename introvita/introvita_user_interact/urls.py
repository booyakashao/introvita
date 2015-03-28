from django.conf.urls import patterns, url
from introvita_user_interact import views

urlpatterns = patterns('',
                       url(r'employer/jobs', views.employer_jobs, name='index'),
                       url(r'jobs/jobdetail/(?P<job_id>\d+)', views.job_detail, name='job_detail'),
                       )