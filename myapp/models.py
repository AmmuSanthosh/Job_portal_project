from django.db import models

# Create your models here.
class candidate(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phonenumber = models.IntegerField(null=True)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200,null=True)

class recruiter(models.Model):
    companyname = models.CharField(max_length=200, null=True)
    companyaddress = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phonenumber = models.IntegerField(null=True)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200,null=True)

class jobs(models.Model):
    jobtype = models.CharField(max_length=200, null=True)
    jobname = models.CharField(max_length=200, null=True)
    vacancies = models.IntegerField(null=True)