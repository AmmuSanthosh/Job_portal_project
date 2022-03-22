from django.contrib import admin
from .models import candidate,recruiter, jobs

# Register your models here.
admin.site.register(candidate)
admin.site.register(recruiter)
admin.site.register(jobs)