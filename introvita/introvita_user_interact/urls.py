from django.conf.urls import patterns, url
from introvita_user_interact import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'register', views.register, name='register'),
    url(r'register/createaccount', views.create_account, name='create_account'),
    url(r'employer/jobs', views.employer_jobs, name='employer_jobs'),
    url(r'jobs/jobdetail/(?P<job_id>\d+)', views.job_detail, name='job_detail'),
    )