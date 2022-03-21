from django.urls import path
from .import views

urlpatterns=[
    #main home page
    path("", views.main_home, name="homepage"),
    #candidate home page
    path("candidate_home/", views.candidate_home, name="candidate_home"),
    #recruiter home page
    path("recruiter_home/", views.recruiter_home, name="recruiter_home"),
    #admin home page
    path("admin_home/", views.admin_home, name="admin_home"),

    #Candidate registeration
    path("candidate_register/", views.candidate_register, name="candidate_register"),
    #view candidates 
    path("register_candidates/", views.register_candidates, name="register_candidates"),
    #detailview of candidate profile
    path("viewcandidate/<str:pk>", views.viewcandidate, name="viewcandidate"),

    #delete candidate profile
    path("delete/<str:pk>",views.delete_candidate, name="delete"),
    #update candidate profile
    path("update_candidate/<str:pk>", views.update_candidate, name="update_candidate"),
    
    #recruiter registeration
    path("recruiter_register/", views.recruiter_register, name="recruiter_register"),
    #view recruiter 
    path("register_recruiters/", views.register_recruiters, name="register_recruiters"),
    #detailview of recruiter profile
    path("viewrecruiter/<str:pk>", views.viewrecruiter, name="viewrecruiter"),

    #delete recruiter profile
    path("delete_recruiter/<str:pk>",views.delete_recruiter, name="delete_recruiter"),
    #update recruiter profile
    path("update_recruiter/<str:pk>", views.update_recruiter, name="update_recruiter"),

    #Candidate login
    path("candidate_login/", views.candidate_login, name="candidate_login"),
    path("loguser/", views.loguser, name="loguser"),

    #recruiter login
    path("recruiter_login/", views.recruiter_login, name="recruiter_login"),
    path("logrecruiter/", views.logrecruiter, name="logrecruiter"),

    #admin login
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logadmin/", views.logadmin, name="logadmin"),
    path("loggedadmin/", views.loggedadmin, name="loggedadmin"),

    #logout
    path("logout/", views.logout, name="logout"),


    #recruiter side : add jobs
    path("add_jobs/", views.add_jobs, name="add_jobs"),
    # view jobs
    path("view_jobs/", views.view_jobs, name="view_jobs"),
    #detailview of job profile
    path("detail_jobview/<str:pk>", views.detail_jobview, name="detail_jobview"),
    
    #delete recruiter profile
    path("delete_job/<str:pk>",views.delete_job, name="delete_job"),
    # update jobs
    path("update_job/<str:pk>", views.update_job, name="update_job"),
    
    #candidate side : Apply jobs
    path("apply_jobs/", views.apply_jobs, name="apply_jobs"),

    #admin side : Add candidates
    path("add_candidates/", views.add_candidates, name="add_candidates"),
    #Add recruiters
    path("add_recruiters/", views.add_recruiters, name="add_recruiters"),
    #view registered candidates
    path("admin_candidates/", views.admin_candidates, name="admin_candidates"),
    #view registered recruiters
    path("admin_recruiters/", views.admin_recruiters, name="admin_recruiters"),
]