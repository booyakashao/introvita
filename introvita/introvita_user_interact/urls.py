from django.conf.urls import patterns, url
from introvita_user_interact import views

urlpatterns = patterns('',
                       url(r'employer/jobs/', views.employerJobs, name='index'),
                       )