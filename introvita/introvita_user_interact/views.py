from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from introvita_user_interact.models import *

# Create your views here.


def index(request):
    template = loader.get_template('landing_page/index.html')
    context = RequestContext(request, {
         'response_message': 'Splash Page',
    })
    return HttpResponse(template.render(context))


def register(request):
    template = loader.get_template('register/register1.html')
    context = RequestContext(request, {
        'response_message': 'Registration Context',
        'states': State.objects.all(),
    })
    return HttpResponse(template.render(context))


def create_account(request):
    return ""


def employer_jobs(request):
    template = loader.get_template('employer/jobs.html')
    context = RequestContext(request, {
        'response_message': 'Employer Jobs Response.',
    })
    return HttpResponse(template.render(context))


def employer_create_job(request):
    template = loader.get_template('employer/create_job.html')
    context = RequestContext(request, {
        'response_message': 'New Job'
    })
    return HttpResponse(template.render(context))


def job_detail(request, job_id):
    template = loader.get_template('jobs/jobdetail.html')
    context = RequestContext(request, {
        'response_message': 'Job Details Response. Job ID: ' + job_id,
    })
    return HttpResponse(template.render(context))

