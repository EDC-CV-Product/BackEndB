from email.mime import application
from urllib import request
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import status

from .serializers import *
from django_filters import rest_framework as filters

from rest_framework import filters
from rest_framework import generics


# API that used to retun all Data In the Database Table
class UserApiView(APIView):
    serializer_class=UserSerializer
    def get(self,request):
        users=user.objects.all().values()
        return Response({"Message":"Sucess","data":users})

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
        queryset = user.objects.get(id=request.data['user_id'])
        serializer = UserSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class userdetailView(APIView):
    
    def get(self,request,users):
        users=user.objects.filter(id=users)
        serializer_class=UserSerializer(users,many=True)
        return Response(serializer_class.data)

# Searching or Filtering paramater with URL query String search
@api_view(['GET'])
def get_user_by_email(request):
        queryset = user.objects.all()
        email = request.query_params.get('email', None)
        if email is not None:
            print('go it')
            queryset = queryset.filter(email=email)
        serializer = UserSerializer(queryset, many=True)
        return Response({'data': serializer.data})

# API for User Role Starts Here

class UserRoleApiView(APIView):
    serializer_class=UserRoleSerializer
    def get(self,request):
        User_Roles=User_Role.objects.all().values()
        return Response({"Message":"Sucess","data":User_Roles})

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
    
    def get(self,request,User_Roles):
        User_Roles=User_Role.objects.filter(user_role_id=User_Roles)
        serializer_class=UserRoleSerializer(User_Roles,many=True)
        return Response(serializer_class.data)

# API for  Role Starts Here

class RoleApiView(APIView):
    serializer_class=RoleSerializer
    def get(self,request):
        Roles=Role.objects.all().values()
        return Response({"Message":"Sucess","data":Roles})

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
    
    def get(self,request,Roles):
        Roles=Role.objects.filter(role_id=Roles)
        serializer_class=RoleSerializer(Roles,many=True)
        return Response(serializer_class.data)

# API for  Skill Set Starts Here

class SkillsetApiView(APIView):
    serializer_class=SkillsetSerializer
    def get(self,request):
        Skill_Sets=Skill_Set.objects.all().values()
        return Response({"Message":"Sucess","data":Skill_Sets})

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
    
    def get(self,request,Skill_Sets):
        Skill_Sets=Skill_Set.objects.filter(skill_set_id=Skill_Sets)
        serializer_class=SkillsetSerializer(Skill_Sets,many=True)
        return Response(serializer_class.data)

# API for  Job Platform Starts Here

class JobPlatformApiView(APIView):
    serializer_class=jobplatformSerializer
    def get(self,request):
        job_platform=job_platforms.objects.all().values()
        return Response({"Message":"Sucess","data":job_platform})

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
    
    def get(self,request,job_platform):
        job_platform=job_platforms.objects.filter(job_platform_id=job_platform)
        serializer_class=jobplatformSerializer(job_platform,many=True)
        return Response(serializer_class.data)


# API for  Companey Starts Here

class CompanyApiView(APIView):
    serializer_class=CompanySerializer
    def get(self,request):
        Companys=Company.objects.all().values()
        return Response({"Message":"Sucess","data":Companys})

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
    
    def get(self,request,Companys):
        Companys=Company.objects.filter(companey_id=Companys)
        serializer_class=CompanySerializer(Companys,many=True)
        return Response(serializer_class.data)


# API for  applicant_cv Starts Here

class applicant_cvApiView(APIView):
    serializer_class=Applicant_cvSerializer
    def get(self,request):
        applicant_cvs=applicant_cv.objects.all().values()
        return Response({"Message":"Sucess","data":applicant_cvs})

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
    
    def get(self,request,applicant_cvs):
        applicant_cvs=applicant_cv.objects.filter(applicant_id=applicant_cvs)
        serializer_class=Applicant_cvSerializer(applicant_cvs,many=True)
        return Response(serializer_class.data)


# API for  Experiance Starts Here

class ExperianceApiView(APIView):
    serializer_class=ExperianceSerializer
    def get(self,request):
        Experiences=Experience.objects.all().values()
        return Response({"Message":"Sucess","data":Experiences})

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
    
    def get(self,request,Experiences):
        Experiences=Experience.objects.filter(experiance_id=Experiences)
        serializer_class=ExperianceSerializer(Experiences,many=True)
        return Response(serializer_class.data)


# API for  Education Starts Here

class EducationApiView(APIView):
    serializer_class=EducationSerializer
    def get(self,request):
        Educations=Education.objects.all().values()
        return Response({"Message":"Sucess","data":Educations})

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
    
    def get(self,request,Educations):
        Educations=Education.objects.filter(education_id=Educations)
        serializer_class=EducationSerializer(Educations,many=True)
        return Response(serializer_class.data)


# API for  Job Starts Here

class JobApiView(APIView):
    serializer_class=JobSerializer
    def get(self,request):
        Jobs=Job.objects.all().values()
        return Response({"Message":"Sucess","data":Jobs})

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
    
    def get(self,request,Jobs):
        Jobs=Job.objects.filter(job_id=Jobs)
        serializer_class=JobSerializer(Jobs,many=True)
        return Response(serializer_class.data)

@api_view(['GET'])
def get_jobs_by_job_position(request):
        queryset = Job.objects.all()
        job_position = request.query_params.get('job_position', None)
        if job_position is not None:
            print('go it')
            queryset = queryset.filter(job_position=job_position)
        serializer = JobSerializer(queryset, many=True)
        return Response({'data': serializer.data})

# API for  job_category Starts Here

class JobCategoryApiView(APIView):
    serializer_class=JobcategorySerializer
    def get(self,request):
        job_categorys=job_category.objects.all().values()
        return Response({"Message":"Sucess","data":job_categorys})

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
    
    def get(self,request,job_categorys):
        job_categorys=job_category.objects.filter(job_category_id=job_categorys)
        serializer_class=JobcategorySerializer(job_categorys,many=True)
        return Response(serializer_class.data)

# API for  Application Starts Here

class ApplicationApiView(APIView):
    serializer_class=ApplicationSerializer
    def get(self,request):
        Applications=Application.objects.all().values()
        return Response({"Message":"Sucess","data":Applications})

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
    
    def get(self,request,Applications):
        Applications=Application.objects.filter(application_id=Applications)
        serializer_class=ApplicationSerializer(Applications,many=True)
        return Response(serializer_class.data)

@api_view(['GET'])
def get_application_by_user_id(request):
        queryset = Application.objects.all()
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            print('go it')
            queryset = queryset.filter(user_id=user_id)
        serializer = ApplicationSerializer(queryset, many=True)
        return Response({'data': serializer.data})

# API for  Applicant_Document Starts Here

class Applicant_DocumentApiView(APIView):
    serializer_class=ApplicatDocumentSerializer
    def get(self,request):
        Applicant_Documents=Applicant_Document.objects.all().values()
        return Response({"Message":"Sucess","data":Applicant_Documents})

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

class Applicant_DocumentdetailView(generics.ListAPIView):
    def get(self,request,Applicant_Documents):
        Applicant_Documents=Applicant_Document.objects.filter(applicant_document_id=Applicant_Documents)
        serializer_class=ApplicatDocumentSerializer(Applicant_Documents,many=True)
        return Response(serializer_class.data)

@api_view(['GET'])
def usered(request):
        queryset = Applicant_Document.objects.all()
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            print('go it')
            queryset = queryset.filter(user_id=user_id)
        serializer = ApplicatDocumentSerializer(queryset, many=True)
        return Response({'data': serializer.data})
       
# API for  candidate_Evaluation Starts Here
class Candidate_EvaluationApiView(APIView):
    serializer_class=candidate_EvaluationSerializer
    def get(self,request):
        candidate_Evaluations=candidate_Evaluation.objects.all().values()
        return Response({"Message":"Sucess","data":candidate_Evaluations})

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
    
    def get(self,request,candidate_Evaluations):
        candidate_Evaluations=candidate_Evaluation.objects.filter(candidate_evaluation_id=candidate_Evaluations)
        serializer_class=candidate_EvaluationSerializer(candidate_Evaluations,many=True)
        return Response(serializer_class.data)
# to search Candidate evaluation using Job ID
@api_view(['GET'])
def get_candidate_by_job_id(request):
        queryset = candidate_Evaluation.objects.all()
        job_id = request.query_params.get('job_id', None)
        if job_id is not None:
            print('go it')
            queryset = queryset.filter(job_id=job_id)
        serializer = candidate_EvaluationSerializer(queryset, many=True)
        return Response({'data': serializer.data})

# API for  Job_Description_Document Starts Here

class Job_Description_DocumentApiView(APIView):
    serializer_class=jobDiscriptionSerializer
    def get(self,request):
        Job_Description_Documents=Job_Description_Document.objects.all().values()
        return Response({"Message":"Sucess","data":Job_Description_Documents})

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
    
    def get(self,request,Job_Description_Documents):
        Job_Description_Documents=Job_Description_Document.objects.filter(job_description_id=Job_Description_Documents)
        serializer_class=jobDiscriptionSerializer(Job_Description_Documents,many=True)
        return Response(serializer_class.data)
