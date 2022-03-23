from django.urls import path
from .import views

urlpatterns=[
    #Main home page
    path("", views.main_home, name="homepage"),
    
    #Candidate home page
    path("candidate_home/", views.candidate_home, name="candidate_home"),
    
    #Candidate registeration
    path("candidate_register/", views.candidate_register, name="candidate_register"),
    
    #Candidate login
    path("candidate_login/", views.candidate_login, name="candidate_login"),
    path("loguser/", views.loguser, name="loguser"),
    
    #View candidates profile
    path("register_candidates/", views.register_candidates, name="register_candidates"),
    
    #Candidate side : Apply jobs
    path("apply_jobs/", views.apply_jobs, name="apply_jobs"),
    #Applied jobs
    path("job_apply/<str:pk>", views.job_apply, name="job_apply"),

    #Recruiter home page
    path("recruiter_home/", views.recruiter_home, name="recruiter_home"),
    
    #Recruiter registeration
    path("recruiter_register/", views.recruiter_register, name="recruiter_register"),
    
    #Recruiter login
    path("recruiter_login/", views.recruiter_login, name="recruiter_login"),
    path("logrecruiter/", views.logrecruiter, name="logrecruiter"),
    
    #View recruiter 
    path("register_recruiters/", views.register_recruiters, name="register_recruiters"),
    
    #Recruiter side : add jobs
    path("add_jobs/", views.add_jobs, name="add_jobs"),
    
    #View jobs list
    path("jobs_list/", views.jobs_list, name="jobs_list"),


    #Admin home page
    path("admin_home/", views.admin_home, name="admin_home"),
    
    #Admin login
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logadmin/", views.logadmin, name="logadmin"),
    path("loggedadmin/", views.loggedadmin, name="loggedadmin"),
    
    #Admin side : Add candidates
    path("add_candidates/", views.add_candidates, name="add_candidates"),
    
    #Add recruiters
    path("add_recruiters/", views.add_recruiters, name="add_recruiters"),


    #Admin side : view registered candidates
    path("admin_candidates/", views.admin_candidates, name="admin_candidates"),
    
    #Delete candidate profile
    path("delete_candidate/<str:pk>",views.delete_candidate, name="delete_candidate"),
    
    #Update candidate profile
    path("update_candidate/<str:pk>", views.update_candidate, name="update_candidate"),
    

    #Admin side : view registered recruiters
    path("admin_recruiters/", views.admin_recruiters, name="admin_recruiters"),
    
    #Delete recruiter profile
    path("delete_recruiter/<str:pk>",views.delete_recruiter, name="delete_recruiter"),
    
    #Update recruiter profile
    path("update_recruiter/<str:pk>", views.update_recruiter, name="update_recruiter"),
    

    #Admin side : view jobs
    path("view_jobs/", views.view_jobs, name="view_jobs"),
    
    #Delete jobs
    path("delete_job/<str:pk>",views.delete_job, name="delete_job"),
    
    #Update jobs
    path("update_job/<str:pk>", views.update_job, name="update_job"),


    #Logout
    path("logout/", views.logout, name="logout"),
   
    
]