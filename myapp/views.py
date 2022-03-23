from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as log
from .forms import CandidateRegisterForm, JobListForm, RecruiterRegisterForm
from .models import candidate, jobs, recruiter, Application
from django.contrib import auth
from datetime import date
# Create your views here.

#Main home page
def main_home(request):
    return render(request,'main_home.html')

#Candidate home page
def candidate_home(request):
    return render(request,'candidate_home.html')

#Candidate registration
def candidate_register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        username = request.POST.get('username')
        password = request.POST.get('password')
        candidate(firstname=firstname,lastname=lastname,email=email,phonenumber=phonenumber,username=username,password=password).save()
        return redirect('candidate_login')
    return render(request, 'candidate_register.html')

#Candidate login
def candidate_login(request):
    return render(request, 'candidate_login.html')

def loguser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr = candidate.objects.filter(username=username, password=password)
        if cr:

           return  redirect('candidate_home')
        else:
            return render(request, 'candidate_login.html')

    else:
        return render(request, 'candidate_register.html')

#View candidates profile
def register_candidates(request):
    cr = candidate.objects.all()
    return render(request, 'register_candidates.html',{'cr':cr})

#Candidate side : Apply jobs
def apply_jobs(request):
    cr = jobs.objects.all()
    return render(request, 'apply_jobs.html',{'cr':cr})

#Applied jobs
def job_apply(request, pk):
    applicant = candidate.objects.get(user=request.user)
    job = jobs.objects.get(id=pk)
    date1 = date.today()

    Application.objects.create(job=job, applicant=applicant, apply_date=date1)
    return render('candidate_home')
    

#Recruiter home page
def recruiter_home(request):
    return render(request,'recruiter_home.html')

#Recruiter registration
def recruiter_register(request):
    if request.method == 'POST':
        companyname = request.POST.get('companyname')
        companyaddress = request.POST.get('companyaddress')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        username = request.POST.get('username')
        password = request.POST.get('password')
        recruiter(companyname=companyname,companyaddress=companyaddress,email=email,phonenumber=phonenumber,username=username,password=password).save()
        return redirect('recruiter_login')
    return render(request, 'recruiter_register.html')

#Recruiter login
def recruiter_login(request):
    return render(request, 'recruiter_login.html')

def logrecruiter(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr = recruiter.objects.filter(username=username, password=password)
        if cr:

           return  redirect('recruiter_home')
        else:
            return render(request, 'recruiter_login.html')

    else:
        return render(request, 'recruiter_register.html')

#View recruiter 
def register_recruiters(request):
    cr = recruiter.objects.all()
    return render(request, 'register_recruiters.html',{'cr':cr})

#Recruiter side : add jobs
def add_jobs(request):
    if request.method == 'POST':
        jobtype = request.POST.get('jobtype')
        jobname = request.POST.get('jobname')
        vacancies = request.POST.get('vacancies')
        jobs(jobtype=jobtype,jobname=jobname,vacancies=vacancies).save()
    return render(request, 'add_jobs.html')

#View jobs list
def jobs_list(request):
    cr = jobs.objects.all()
    return render(request, 'jobs_list.html',{'cr':cr})


#Admin home page
def admin_home(request):
    return render(request,'admin_home.html')

#Admin login
def admin_login(request):
    return render(request, 'admin_login.html')

def logadmin(request):
    if request.method == 'POST':
        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log(request, user)
            return redirect('loggedadmin')
        else:
            return render(request,'main_home.html')
    else:
        return render(request, 'main_home.html')

def loggedadmin(request):
    return render(request, 'admin_home.html')

#Admin side : Add candidates
def add_candidates(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        username = request.POST.get('username')
        password = request.POST.get('password')
        candidate(firstname=firstname,lastname=lastname,email=email,phonenumber=phonenumber,username=username,password=password).save()
    return render(request, 'add_candidates.html')

#Add recruiters
def add_recruiters(request):
    if request.method == 'POST':
        companyname = request.POST.get('companyname')
        companyaddress = request.POST.get('companyaddress')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        username = request.POST.get('username')
        password = request.POST.get('password')
        recruiter(companyname=companyname,companyaddress=companyaddress,email=email,phonenumber=phonenumber,username=username,password=password).save()
    return render(request, 'add_recruiters.html')


#Admin side : view registered candidates
def admin_candidates(request):
    cr = candidate.objects.all()
    return render(request, 'admin_candidates.html',{'cr':cr})

#Delete candidate profile
def delete_candidate(request,pk):
    cr = candidate.objects.get(id = pk)
    cr.delete()
    return redirect('admin_candidates')

#Update candidate profile
def update_candidate(request,pk):
    cr = candidate.objects.get(id = pk)
    form = CandidateRegisterForm(instance= cr)
    if request.method == 'POST':
        form = CandidateRegisterForm(request.POST, instance=cr)
        if form.is_valid:
            form.save()
            return redirect('admin_candidates')
    return render(request, 'update_candidate.html', {'form':form})



#Admin side : view registered recruiters
def admin_recruiters(request):
    cr = recruiter.objects.all()
    return render(request, 'admin_recruiters.html',{'cr':cr})

#Delete recruiter profile
def delete_recruiter(request,pk):
    cr = recruiter.objects.get(id = pk)
    cr.delete()
    return redirect('admin_recruiters')

#Update recruiter profile
def update_recruiter(request,pk):
    cr = recruiter.objects.get(id = pk)
    form = RecruiterRegisterForm(instance= cr)
    if request.method == 'POST':
        form = RecruiterRegisterForm(request.POST, instance=cr)
        if form.is_valid:
            form.save()
            return redirect('admin_recruiters')
    return render(request, 'update_recruiter.html', {'form':form})


#Admin side : view jobs
def view_jobs(request):
    cr = jobs.objects.all()
    return render(request, 'view_jobs.html',{'cr':cr})

#Delete jobs profile
def delete_job(request,pk):
    cr = jobs.objects.get(id = pk)
    cr.delete()
    return redirect('view_jobs')

#Update jobs profile
def update_job(request,pk):
    cr = jobs.objects.get(id = pk)
    form = JobListForm(instance= cr)
    if request.method == 'POST':
        form = JobListForm(request.POST, instance=cr)
        if form.is_valid:
            form.save()
            return redirect('view_jobs')
    return render(request, 'update_job.html', {'form':form})


#logout
def logout(request):
    auth.logout(request)
    return redirect('main_home')

