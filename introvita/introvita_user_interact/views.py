from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def employer_jobs(request):
    template = loader.get_template('employer/jobs.html')
    context = RequestContext(request, {
        'response_message': 'Employer Jobs Response.',
    })
    return HttpResponse(template.render(context))


def job_detail(request, job_id):
    template = loader.get_template('jobs/jobdetail.html')
    context = RequestContext(request, {
        'response_message': 'Job Details Response. Job ID: ' + job_id,
    })
    return HttpResponse(template.render(context))