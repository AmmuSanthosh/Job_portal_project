from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as log
from .forms import CandidateRegisterForm, JobListForm, RecruiterRegisterForm
from .models import candidate, jobs, recruiter
from django.contrib import auth
# Create your views here.

#main home page
def main_home(request):
    return render(request,'main_home.html')

#candidate home page
def candidate_home(request):
    return render(request,'candidate_home.html')

#recruiter home page
def recruiter_home(request):
    return render(request,'recruiter_home.html')

#admin home page
def admin_home(request):
    return render(request,'admin_home.html')

#candidate registration
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

#view candidate 
def register_candidates(request):
    cr = candidate.objects.all()
    return render(request, 'register_candidates.html',{'cr':cr})

#view candidate profile
def viewcandidate(request,pk):
    cr = candidate.objects.get(id=pk)
    return render(request, 'view_candidate.html',{'cr':cr})

#delete candidate profile
def delete_candidate(request,pk):
    cr = candidate.objects.get(id = pk)
    cr.delete()
    return redirect('register_candidates')

#update candidate profile
def update_candidate(request,pk):
    cr = candidate.objects.get(id = pk)
    form = CandidateRegisterForm(instance= cr)
    if request.method == 'POST':
        form = CandidateRegisterForm(request.POST, instance=cr)
        if form.is_valid:
            form.save()
            return redirect('register_candidates')
    return render(request, 'update_candidate.html', {'form':form})


#candidate login
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

#recruiter registration
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

#view recruiter 
def register_recruiters(request):
    cr = recruiter.objects.all()
    return render(request, 'register_recruiters.html',{'cr':cr})

#view recruiter profile
def viewrecruiter(request,pk):
    cr = recruiter.objects.get(id=pk)
    return render(request, 'view_recruiter.html',{'cr':cr})

#delete recruiter profile
def delete_recruiter(request,pk):
    cr = recruiter.objects.get(id = pk)
    cr.delete()
    return redirect('register_recruiters')

#update recruiter profile
def update_recruiter(request,pk):
    cr = recruiter.objects.get(id = pk)
    form = RecruiterRegisterForm(instance= cr)
    if request.method == 'POST':
        form = RecruiterRegisterForm(request.POST, instance=cr)
        if form.is_valid:
            form.save()
            return redirect('register_recruiters')
    return render(request, 'update_recruiter.html', {'form':form})

#recruiter login
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

#add jobs
def add_jobs(request):
    if request.method == 'POST':
        jobtype = request.POST.get('jobtype')
        jobname = request.POST.get('jobname')
        vacancies = request.POST.get('vacancies')
        jobs(jobtype=jobtype,jobname=jobname,vacancies=vacancies).save()
    return render(request, 'add_jobs.html')

#view jobs profile
def view_jobs(request):
    cr = jobs.objects.all()
    return render(request, 'view_jobs.html',{'cr':cr})

#detailview job profile
def detail_jobview(request,pk):
    cr = jobs.objects.get(id=pk)
    return render(request, 'detail_jobview.html',{'cr':cr})

#delete jobs profile
def delete_job(request,pk):
    cr = jobs.objects.get(id = pk)
    cr.delete()
    return redirect('view_jobs')

#update jobs profile
def update_job(request,pk):
    cr = jobs.objects.get(id = pk)
    form = JobListForm(instance= cr)
    if request.method == 'POST':
        form = JobListForm(request.POST, instance=cr)
        if form.is_valid:
            form.save()
            return redirect('view_jobs')
    return render(request, 'update_job.html', {'form':form})

#apply jobs
def apply_jobs(request):
    cr = jobs.objects.all()
    return render(request, 'apply_jobs.html',{'cr':cr})

#add candidates
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

#add recruiters
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

#admin side : candidates list
def admin_candidates(request):
    cr = candidate.objects.all()
    return render(request, 'admin_candidates.html',{'cr':cr})

#admin side : recruiters list
def admin_recruiters(request):
    cr = candidate.objects.all()
    return render(request, 'admin_recruiters.html',{'cr':cr})

#admin login
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

def logout(request):
    auth.logout(request)
    return redirect('main_home')
