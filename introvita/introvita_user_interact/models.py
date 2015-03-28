from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'State Name: ' + self.name


class Authority(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Authority Name: ' + self.name


class User(models.Model):
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100)
    addressLine1 = models.CharField(max_length=300)
    addressLine2 = models.CharField(max_length=300)
    phoneNumber = models.CharField(max_length=20)
    emailAddress = models.EmailField()
    password = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.ForeignKey(State)
    zipcode = models.IntegerField()
    paymentId = models.CharField(max_length=500)
    company = models.CharField(max_length=100)
    department = models.CharField(max_length=200)
    positionAtCompany = models.CharField(max_length=150)
    authority = models.ForeignKey(Authority)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CandidateAttributes(models.Model):
    passionsAndGoals = models.CharField(max_length=500)
    workProjectDone = models.TextField()
    skills = models.TextField()
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class JobPost(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    about = models.TextField()
    summary = models.TextField()
    qualifications = models.TextField()
    responsibilities = models.TextField()
    employer = models.ForeignKey(User)
    salary = models.CharField(max_length=150)
    limit = models.IntegerField()
    applied = models.IntegerField()
    enabled = models.BooleanField()
    questionsId = models.ForeignKey(Questions)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Question(models.Model):
    questionsId = models.ForeignKey(Questions)
    question = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Question: ' + self.question


class Answer(models.Model):
    questions = models.ForeignKey(Question)
    candidate = models.ForeignKey(User)
    answer = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Answer: ' + self.answer


class ApplicationToJob(models.Model):
    candidate = models.ForeignKey(User)
    jobPost = models.ForeignKey(JobPost)
    applied = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

