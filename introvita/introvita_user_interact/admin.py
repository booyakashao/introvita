from django.contrib import admin
from introvita_user_interact.models import *

# Register your models here.

admin.site.register(State)
admin.site.register(Authority)
admin.site.register(User)
admin.site.register(CandidateAttributes)
admin.site.register(Questions)
admin.site.register(JobPost)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(ApplicationToJob)