"""ATS_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from ATS_APP import views
from rest_framework.urlpatterns import format_suffix_patterns

from ATS_APP.models import *

from ATS_APP.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # Get Registred Useres
    path('users/',views.UserApiView.as_view(),name="User List(GET)"),
    # Filtering Registred Users By Using user id
    path('users/<int:uid>',views.userdetailView.as_view(),name=' User Detailed'),
    #get All Applicant Document from DAtabase Table
    path('Applicant_Document/',views.Applicant_DocumentApiView.as_view(),name="Applicant(GET)"),
    #get Appliccant Document by using Certaim Parameter
    path('Applicant_Document/<int:appid>',views.Applicant_DocumentdetailView.as_view(),name="Applicant Detail View"),

    path('Application/',views.ApplicationApiView.as_view(),name="Application"),# to Get Whole Data From The Database Table
    path('Application/<int:App>',views.ApplicationdetailView.as_view(),name="Application Detail View"),# to searrch by Spesfic Parameter
    
    path('Job/',views.JobApiView.as_view(),name="Job"),
    path('Job/<int:jobid>',views.jobdetailView.as_view(),name="Job Detail View"),

    path('User_Role/',views.UserRoleApiView.as_view(),name="User Role"),
    path('User_Role/<int:urroleid>',views.userroledetailView.as_view(),name="User Role Detail View"),


    path('Role/',views.RoleApiView.as_view(),name="Role"),
    path('Role/<int:roo>',views.roledetailView.as_view(),name="Role Detail View"),


    path('Skill_Set/',views.SkillsetApiView.as_view(),name="Skill"),
    path('Skill_Set/<int:roo>',views.skilldetailView.as_view(),name="Skill Detail View"),

    path('job_platforms/',views.JobPlatformApiView.as_view(),name="Job Platform"),
    path('job_platforms/<int:jobpalt>',views.jobplatdetailView.as_view(),name="Job Platforms Detail View"),


    path('Company/',views.CompanyApiView.as_view(),name="Company"),
    path('Company/<int:compid>',views.CompanydetailView.as_view(),name="Company Detail View"),

    path('applicant_cv/',views.applicant_cvApiView.as_view(),name="Applicant Cv"),
    path('applicant_cv/<int:compid>',views.Applicant_cvdetailView.as_view(),name="applicant Cv Detail View"),

    path('Experience/',views.ExperianceApiView.as_view(),name="Experiance"),
    path('Experience/<int:compid>',views.ExperiancedetailView.as_view(),name="Experiance Detail View"),

    path('Education/',views.EducationApiView.as_view(),name="Education"),
    path('Education/<int:compid>',views.EducationdetailView.as_view(),name="Education Detail View"),

    path('candidate_Evaluation/',views.Candidate_EvaluationApiView.as_view(),name="Candidate Evaluation"),
    path('candidate_Evaluation/<int:compid>',views.CandidateEvaluationdetailView.as_view(),name="Candidate Evaluation Detail View"),

    path('job_category/',views.JobCategoryApiView.as_view(),name="Job Category"),
    path('job_category/<int:compid>',views.job_categorydetailView.as_view(),name="Job Category Detail View"),

    path('Job_dis/',views.Job_Description_DocumentApiView.as_view(),name="Job Category"),
    path('job_dis/<int:compid>',views.JobDiscriptiondetailView.as_view(),name="Job Category Detail View"),


    ]
