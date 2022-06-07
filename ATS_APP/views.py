from email.mime import application
from urllib import request
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import status

from .serializers import *


# API that used to retun all Data In the Database Table
class UserApiView(APIView):
    serializer_class=UserSerializer
    def get(self,request):
        #alluser is variable and user is table name
        users=user.objects.all().values()
        # can also write in one of the following options
        #return Response(serializers.data)
        return Response({"Message":"List of Users","User List":users})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = UserSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

    def put(self, request):
        queryset = user.objects.get(user_id=request.data['user_id'])
        serializer = UserSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class userdetailView(APIView):
    
    def get(self,request,uid):
        users=user.objects.filter(user_id=uid)
        serializer_class=UserSerializer(users,many=True)
        return Response(serializer_class.data)

# API for User Role Starts Here

class UserRoleApiView(APIView):
    serializer_class=UserRoleSerializer
    def get(self,request):
        User_Rolee=User_Role.objects.all().values()
        return Response({"Message":"List of User roles","User Role List":User_Rolee})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = UserRoleSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class userroledetailView(APIView):
    
    def get(self,request,urroleid):
        userroid=User_Role.objects.filter(user_role_id=urroleid)
        serializer_class=UserRoleSerializer(userroid,many=True)
        return Response(serializer_class.data)

# API for  Role Starts Here

class RoleApiView(APIView):
    serializer_class=RoleSerializer
    def get(self,request):
        Rol=Role.objects.all().values()
        return Response({"Message":"List of User roles"," Role List":Rol})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = RoleSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class roledetailView(APIView):
    
    def get(self,request,roo):
        roo=Role.objects.filter(role_id=roo)
        serializer_class=RoleSerializer(roo,many=True)
        return Response(serializer_class.data)

# API for  Skill Set Starts Here

class SkillsetApiView(APIView):
    serializer_class=SkillsetSerializer
    def get(self,request):
        skill=Skill_Set.objects.all().values()
        return Response({"Message":"List of User roles","User Role List":skill})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = SkillsetSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class skilldetailView(APIView):
    
    def get(self,request,skill_det):
        skill_det=Skill_Set.objects.filter(skill_set_id=skill_det)
        serializer_class=SkillsetSerializer(skill_det,many=True)
        return Response(serializer_class.data)

# API for  Job Platform Starts Here

class JobPlatformApiView(APIView):
    serializer_class=jobplatformSerializer
    def get(self,request):
        Job_Plat=job_platforms.objects.all().values()
        return Response({"Message":"List of Job Platforms","Job Platform List":Job_Plat})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = jobplatformSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class jobplatdetailView(APIView):
    
    def get(self,request,jobpalt):
        Job_Plat=job_platforms.objects.filter(job_platform_id=jobpalt)
        serializer_class=jobplatformSerializer(Job_Plat,many=True)
        return Response(serializer_class.data)


# API for  Companey Starts Here

class CompanyApiView(APIView):
    serializer_class=CompanySerializer
    def get(self,request):
        comp=Company.objects.all().values()
        return Response({"Message":"List of companey","companey List":comp})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = CompanySerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class CompanydetailView(APIView):
    
    def get(self,request,urid):
        compid=Company.objects.filter(companey_id=urid)
        serializer_class=CompanySerializer(compid,many=True)
        return Response(serializer_class.data)


# API for  applicant_cv Starts Here

class applicant_cvApiView(APIView):
    serializer_class=Applicant_cvSerializer
    def get(self,request):
        app_cv=applicant_cv.objects.all().values()
        return Response({"Message":"List of applicant cv","applicant cv List":app_cv})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = Applicant_cvSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class Applicant_cvdetailView(APIView):
    
    def get(self,request,urid):
        applicant=applicant_cv.objects.filter(applicant_id=urid)
        serializer_class=Applicant_cvSerializer(applicant,many=True)
        return Response(serializer_class.data)


# API for  Experiance Starts Here

class ExperianceApiView(APIView):
    serializer_class=ExperianceSerializer
    def get(self,request):
        exp=Experience.objects.all().values()
        return Response({"Message":"List of Job Platforms","Job Platform List":exp})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = ExperianceSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class ExperiancedetailView(APIView):
    
    def get(self,request,urid):
        exper=Experience.objects.filter(experiance_id=urid)
        serializer_class=ExperianceSerializer(exper,many=True)
        return Response(serializer_class.data)


# API for  Education Starts Here

class EducationApiView(APIView):
    serializer_class=EducationSerializer
    def get(self,request):
        Edu=Education.objects.all().values()
        return Response({"Message":"List of Job Platforms","Job Platform List":Edu})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = EducationSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class EducationdetailView(APIView):
    
    def get(self,request,urid):
        edu=Education.objects.filter(education_id=urid)
        serializer_class=EducationSerializer(edu,many=True)
        return Response(serializer_class.data)


# API for  Job Starts Here

class JobApiView(APIView):
    serializer_class=JobSerializer
    def get(self,request):
        jobb=Job.objects.all().values()
        return Response({"Message":"List of Job ","Job  List":jobb})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = JobSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class jobdetailView(APIView):
    
    def get(self,request,jobid):
        jobb=Job.objects.filter(job_id=jobid)
        serializer_class=JobSerializer(jobb,many=True)
        return Response(serializer_class.data)

# API for  job_category Starts Here

class JobCategoryApiView(APIView):
    serializer_class=JobcategorySerializer
    def get(self,request):
        Job_cat=job_category.objects.all().values()
        return Response({"Message":"List of job catagory ","Job category":Job_cat})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = JobcategorySerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class job_categorydetailView(APIView):
    
    def get(self,request,urid):
        Job_cat=job_category.objects.filter(job_category_id=urid)
        serializer_class=JobcategorySerializer(Job_cat,many=True)
        return Response(serializer_class.data)

# API for  Application Starts Here

class ApplicationApiView(APIView):
    serializer_class=ApplicationSerializer
    def get(self,request):
        Apps=Application.objects.all().values()
        return Response({"Message":"List of Application ","Application":Apps})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = ApplicationSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using UserId Only
class ApplicationdetailView(APIView):
    
    def get(self,request,App):
        Apps=Application.objects.filter(application_id=App)
        serializer_class=ApplicationSerializer(Apps,many=True)
        return Response(serializer_class.data)

# API for  Applicant_Document Starts Here

class Applicant_DocumentApiView(APIView):
    serializer_class=ApplicatDocumentSerializer
    def get(self,request):
        Appdoc=Applicant_Document.objects.all().values()
        return Response({"Message":"List of Applicant_Document ","Applicant_Document":Appdoc})

# to Create Form and POST data to Table

    def post(self, request):
        serializer_obj = ApplicatDocumentSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class Applicant_DocumentdetailView(APIView):
    
    def get(self,request,appid):
        Appdoc=Applicant_Document.objects.filter(applicant_document_id=appid)
        serializer_class=ApplicatDocumentSerializer(Appdoc,many=True)
        return Response(serializer_class.data)

# API for  candidate_Evaluation Starts Here

class Candidate_EvaluationApiView(APIView):
    serializer_class=candidate_EvaluationSerializer
    def get(self,request):
        can=candidate_Evaluation.objects.all().values()
        return Response({"Message":"List of Candidate_evaluation ","Candidate_evaluation":can})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = candidate_EvaluationSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class CandidateEvaluationdetailView(APIView):
    
    def get(self,request,urid):
        can=candidate_Evaluation.objects.filter(candidate_evaluation_id=urid)
        serializer_class=candidate_EvaluationSerializer(can,many=True)
        return Response(serializer_class.data)

# API for  Job_Description_Document Starts Here

class Job_Description_DocumentApiView(APIView):
    serializer_class=jobDiscriptionSerializer
    def get(self,request):
        Job_dis=Job_Description_Document.objects.all().values()
        return Response({"Message":"List of Job_Description_Document ","Job_Description_Document":Job_dis})

# to Create Form and POST data to Table
    def post(self, request):
        serializer_obj = jobDiscriptionSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class JobDiscriptiondetailView(APIView):
    
    def get(self,request,urid):
        job_dis=Job_Description_Document.objects.filter(job_description_id=urid)
        serializer_class=jobDiscriptionSerializer(job_dis,many=True)
        return Response(serializer_class.data)
