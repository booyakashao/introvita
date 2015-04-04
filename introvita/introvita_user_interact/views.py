from django.shortcuts import render, get_object_or_404
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
    template = loader.get_template('register/register2.html')

    new_user = User()
    new_user.firstName = request.POST['firstName']
    new_user.middleName = request.POST['middleName']
    new_user.lastName = request.POST['lastName']
    new_user.addressLine1 = request.POST['addressLine1']
    new_user.addressLine2 = request.POST['addressLine2']
    new_user.city = request.POST['city']
    new_user.state = State.objects.get(name=request.POST['state'])
    new_user.zipcode = request.POST['zip']
    new_user.phoneNumber = request.POST['phoneNumber']
    new_user.emailAddress = request.POST['emailAddress']
    new_user.password = request.POST['password']
    new_user.authority = Authority.objects.get(name="ROLE_USER")
    User.save(new_user)

    context = RequestContext(request, {
        'response_message': 'Created a new user'
    })
    return HttpResponse(template.render(context))


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

