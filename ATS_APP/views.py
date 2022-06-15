from email.mime import application
from urllib import request, response
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
from django.db.models import Q
from ATS_Project import settings

import os
from .resume_scan import *
from .utils import *


# API that used to retun all Data In the Database Table
class UserApiView(APIView):
    serializer_class=UserSerializer
    def get(self,request):
        users=user.objects.all().values()
        return Response({"Message":"Success","data":users})

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
# Delete User Using user_id
    def delete(self, req):
        id = req.query_params.get('id', None)
        print(id)
        if id:
            queryset = user.objects.filter(id=id)
            if queryset:
                queryset.delete()
                return Response({"Message": "Success"}, status=status.HTTP_200_OK)
            else:
                return Response({"Message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    # function to update the detail of the data found in the database
    def put(self, request):
        queryset = user.objects.get(id=request.data['id'])
        serializer = UserSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)
@api_view(['GET'])
def search_users(req):
    queryset = user.objects.all()
    first_name = ''
    middle_name = ''
    last_name = ''
    first_name_q = req.query_params.get('first_name',None)
    if first_name_q:
        first_name=first_name_q
    middle_name_q = req.query_params.get('middle_name',None)
    if middle_name_q:
        middle_name=middle_name_q
    last_name_q = req.query_params.get('last_name',None)
    if last_name_q:
        last_name=last_name_q
    #if first_name is not None:
     #  first_name=''
    queryset = queryset.filter(Q(first_name__icontains=first_name)
                               | Q(middle_name__icontains= middle_name)
                               | Q(last_name__icontains= last_name ))
    print('result', len(queryset))
    serializer = UserSerializer(queryset, many=True)
    return Response({'data': serializer.data})

# API used to retrive User Detail Using User Id Only
class userdetailView(APIView):

    def get(self, request, Jobs):
        users = user.objects.get(id=users)
        serializer_class = UserSerializer(users)
        return Response({'Message': 'Success', 'data': serializer_class.data})

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
        queryset=User_Role.objects.all()
        user_role_ser = UserRoleSerializer(queryset, many=True)
        return Response({"Message":"Success","data":user_role_ser.data})
   
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
    def put(self, request):
        queryset = User_Role.objects.get(user_role_id=request.data['user_role_id'])
        serializer = UserRoleSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

    #Delete User role Using User ID
    """def delete(self, request):
            queryset=User_Role.objects.filter(user_role_id=request.data['user_id'])
            print(queryset)
            if queryset:
                    queryset.delete()
                    return Response({"Message":"Success"}, status=status.HTTP_200_OK)
            else:
                    return Response({"Message":"Not Found"}, status=status.HTTP_404_NOT_FOUND)"""
        # Delete User role Using User ID
    def delete(self, req):
        user_id = req.query_params.get('user_id', None)
        print(user_id)
        if user_id:
            queryset = User_Role.objects.filter(user=user_id)
            if queryset:
                queryset.delete()
                return Response({"Message": "Success"}, status=status.HTTP_200_OK)
            else:
                return Response({"Message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
      # return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# API used to retrive User Detail Using User Id Only
class userroledetailView(APIView):
    
    def get(self, request, User_Roles):
        User_Roles = User_Role.objects.get(user_role_id=User_Roles)
        serializer_class = UserRoleSerializer(User_Roles)
        return Response({'Message': 'Success', 'data': serializer_class.data})

# search and remove by using User_id
@api_view(['GET'])
def get_by_id(request):
        queryset = User_Role.objects.all()
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            print('go it')
            queryset = queryset.filter(user_id=user_id)
        serializer = UserRoleSerializer(queryset, many=True)
        return Response({'data': serializer.data})
# remove by using User Id from user roles

# API for  Role Starts Here

class RoleApiView(APIView):
    serializer_class=RoleSerializer
    def get(self,request):
        Roles=Role.objects.all().values()
        return Response({"Message":"Success","data":Roles})

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
#to update the detail of the based on the given data
    def put(self, request):
        queryset = Role.objects.get(role_id=request.data['role_id'])
        serializer = RoleSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class roledetailView(APIView):
    
    #def get(self,request,Roles):
      #  Roles=Role.objects.filter(role_id=Roles)
       # serializer_class=RoleSerializer(Roles,many=True)
       # return Response(serializer_class.data)

    def get(self, request, Roles):
        Roles = Role.objects.get(role_id=Roles)
        serializer_class = RoleSerializer(Roles)
        return Response({'Message': 'Success', 'data': serializer_class.data})

# API for  Skill Set Starts Here

class SkillsetApiView(APIView):
    serializer_class=SkillsetSerializer
    def get(self,request):
        Skill_Sets=Skill_Set.objects.all().values()
        return Response({"Message":"Success","data":Skill_Sets})

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
    #to update the detail of the based on the given data
    def put(self, request):
        queryset = Skill_Set.objects.get(skill_set_id=request.data['skill_set_id'])
        serializer = SkillsetSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)


# API used to retrive User Detail Using User Id Only
class skilldetailView(APIView):
    
    #def get(self,request,Skill_Sets):
     #   Skill_Sets=Skill_Set.objects.filter(skill_set_id=Skill_Sets)
      #  serializer_class=SkillsetSerializer(Skill_Sets,many=True)
       # return Response(serializer_class.data)

    def get(self, request, Skill_Sets):
        Skill_Sets = Skill_Set.objects.get(skill_set_id=Skill_Sets)
        serializer_class = SkillsetSerializer(Skill_Sets)
        return Response({'Message': 'Success', 'data': serializer_class.data})
# API for  Job Platform Starts Here

class JobPlatformApiView(APIView):
    serializer_class=jobplatformSerializer
    def get(self,request):
        job_platform=job_platforms.objects.all().values()
        return Response({"Message":"Success","data":job_platform})

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

      #to update the detail of the based on the given data
    def put(self, request):
        queryset = job_platforms.objects.get(job_platform_id=request.data['job_platform_id'])
        serializer = jobplatformSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class jobplatdetailView(APIView):
    
    def get(self, request, job_platform):
        job_platform = job_platforms.objects.get(job_platform_id=job_platform)
        serializer_class = SkillsetSerializer(job_platform)
        return Response({'Message': 'Success', 'data': serializer_class.data})

# API for  Companey Starts Here

class CompanyApiView(APIView):
    serializer_class=CompanySerializer
    def get(self,request):
        Companys=Company.objects.all().values()
        return Response({"Message":"Success","data":Companys})

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

       #to update the detail of the based on the given data
    def put(self, request):
        queryset = Company.objects.get(companey_id=request.data['companey_id'])
        serializer = CompanySerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class CompanydetailView(APIView):

    def get(self, request, Companys):
        Companys = Company.objects.get(companey_id=Companys)
        serializer_class = CompanySerializer(Companys)
        return Response({'Message': 'Success', 'data': serializer_class.data})

# API for  applicant_cv Starts Here

class applicant_cvApiView(APIView):
    serializer_class=Applicant_cvSerializer
    def get(self,request):
        applicant_cvs=applicant_cv.objects.all().values()
        return Response({"Message":"Success","data":applicant_cvs})

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

        #to update the detail of the based on the given data
    def put(self, request):
        queryset = applicant_cv.objects.get(applicant_id=request.data['applicant_id'])
        serializer = Applicant_cvSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class Applicant_cvdetailView(APIView):
    
    def get(self, request, Companys):
        applicant_cvs = applicant_cv.objects.get(applicant_id=applicant_cvs)
        serializer_class = Applicant_cvSerializer(applicant_cvs)
        return Response({'Message': 'Success', 'data': serializer_class.data})

# API for  Experiance Starts Here

class ExperianceApiView(APIView):
    serializer_class=ExperianceSerializer
    def get(self,request):
        Experiences=Experience.objects.all().values()
        return Response({"Message":"Success","data":Experiences})

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

         #to update the detail of the based on the given data
    def put(self, request):
        queryset = Experience.objects.get(experiance_id=request.data['experiance_id'])
        serializer = ExperianceSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class ExperiancedetailView(APIView):
    
    def get(self,request,Experiences):
        Experiences=Experience.objects.get(experiance_id=Experiences)
        serializer_class=ExperianceSerializer(Experiences)
        return Response({'Message': 'Success', 'data': serializer_class.data})
# API for  Education Starts Here

class EducationApiView(APIView):
    serializer_class=EducationSerializer
    def get(self,request):
        Educations=Education.objects.all().values()
        return Response({"Message":"Success","data":Educations})

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
#update operation on data from database based on the the primary Key
    def put(self, request):
        queryset = Education.objects.get(education_id=request.data['education_id'])
        serializer = EducationSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)
# API used to retrive User Detail Using User Id Only
class EducationdetailView(APIView):
    
    def get(self,request,Educations):
        Educations=Education.objects.get(education_id=Educations)
        serializer_class=EducationSerializer(Educations)
        return Response({'Message': 'Success', 'data': serializer_class.data})

# API for  Job Starts Here

class JobApiView(APIView):
    serializer_class=JobSerializer
    def get(self,request):
        Jobs=Job.objects.all().values()
        return Response({"Message":"Success","data":Jobs})

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
# deleting Job Using User_ID
    def delete(self, request):
            queryset=Job.objects.filter(job_id=request.data['job_id'])
            print(queryset)
            if queryset:
                    queryset.delete()
                    return Response({"Message":"Success"}, status=status.HTTP_200_OK)
            else:
                    return Response({"Message":"Not Found"}, status=status.HTTP_404_NOT_FOUND)

    #update operation on data from database based on the the primary Key
    def put(self, request):
        queryset = Job.objects.get(job_id=request.data['job_id'])
        serializer = JobSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class jobdetailView(APIView):

    def get(self, request, Jobs):
        queryset = Job.objects.get(job_id=Jobs)
        serializer_class = JobSerializer(queryset)
        return Response({'Message': 'Success', 'data': serializer_class.data})

@api_view(['GET'])
def get_jobs_by_job_position(request):
    queryset = Job.objects.all()
    job_position = request.query_params.get('job_position', None)
    if job_position is not None:
        print('go it')
        queryset = queryset.filter(Q(job_position__icontains=job_position))
    serializer = JobSerializer(queryset, many=True)
    return Response({'data': serializer.data})
# API for  job_category Starts Here

class JobCategoryApiView(APIView):
    serializer_class=JobcategorySerializer
    def get(self,request):
        job_categorys=job_category.objects.all().values()
        return Response({"Message":"Success","data":job_categorys})

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

     #update operation on data from database based on the the primary Key
    def put(self, request):
        queryset = job_category.objects.get(job_category_id=request.data['job_category_id'])
        serializer = JobcategorySerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class job_categorydetailView(APIView):
    
    def get(self,request,job_categorys):
        job_categorys=job_category.objects.get(job_category_id=job_categorys)
        serializer_class=JobcategorySerializer(job_categorys)
        return Response({'Message': 'Success', 'data': serializer_class.data})

# API for  Application Starts Here

class ApplicationApiView(APIView):
    serializer_class=ApplicationSerializer
    def get(self,request):
        Applications=Application.objects.all().values()
        return Response({"Message":"Success","data":Applications})

# to Create Form and POST data to Table and delete duplicate value
    def post(self, request):
        serializer_obj = ApplicationSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                previous_apps=Application.objects.filter(user=request.data['user'],job=request.data['job'])
                if previous_apps is not None:
                     previous_apps.delete()
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)

    #Delete Application Using Using User ID
    def delete(self, req):
        user_id = req.query_params.get('user_id', None)
        print(user_id)
        if user_id:
            queryset = Application.objects.filter(user=user_id)
            if queryset:
                queryset.delete()
                return Response({"Message": "Success"}, status=status.HTTP_200_OK)
            else:
                return Response({"Message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
     #update operation on data from database based on the the primary Key
    def put(self, request):
        queryset = Application.objects.get(application_id=request.data['application_id'])
        serializer = ApplicationSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)
# Deleting Applications using User ID


# API used to retrive User Detail Using UserId Only
class ApplicationdetailView(APIView):
    
    def get(self,request,Applications):
        Applications=Application.objects.get(application_id=Applications)
        serializer_class=ApplicationSerializer(Applications)
        return Response({'Message': 'Success', 'data': serializer_class.data})

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
        return Response({"Message":"Success","data":Applicant_Documents})

# to Create Form and POST data to Table

    def post(self, request):
        serializer_obj = ApplicatDocumentSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                previous_docs=Applicant_Document.objects.filter(user=request.data['user'])
                print(previous_docs)
                if previous_docs is not None:
                    previous_docs.delete()
                serializer_obj.save()
                return Response(serializer_obj.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer_obj.errors, status.HTTP_404_NOT_FOUND)
    #Delete Application Document Using User ID
    """def delete(self, request):
            queryset=Applicant_Document.objects.filter(applicant_document_id=request.data['user_id'])
            print(queryset)
            if queryset:
                    queryset.delete()
                    return Response({"Message":"Success"}, status=status.HTTP_200_OK)
            else:
                    return Response({"Message":"Not Found"}, status=status.HTTP_404_NOT_FOUND)"""
    def delete(self, req):
        user_id = req.query_params.get('user_id', None)
        print(user_id)
        if user_id:
            queryset = Applicant_Document.objects.filter(user=user_id)
            if queryset:
                queryset.delete()
                return Response({"Message": "Success"}, status=status.HTTP_200_OK)
            else:
                return Response({"Message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
      #update operation on data from database based on the the primary Key
    def put(self, request):
        queryset = Applicant_Document.objects.get(applicant_document_id=request.data['user_id'])
        serializer = ApplicatDocumentSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only

class Applicant_DocumentdetailView(generics.ListAPIView):
    def get(self,request,Applicant_Documents):
        Applicant_Documents=Applicant_Document.objects.get(applicant_document_id=Applicant_Documents)
        serializer_class=ApplicatDocumentSerializer(Applicant_Documents)
        return Response({'Message': 'Success', 'data': serializer_class.data})

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
        return Response({"Message":"Success","data":candidate_Evaluations})

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

      #update operation on data from database based on the the primary Key
    def put(self, request):
        queryset = candidate_Evaluation.objects.get(candidate_evaluation_id=request.data['candidate_evaluation_id'])
        serializer = candidate_EvaluationSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class CandidateEvaluationdetailView(APIView):
    
    def get(self,request,candidate_Evaluations):
        candidate_Evaluations=candidate_Evaluation.objects.get(candidate_evaluation_id=candidate_Evaluations)
        serializer_class=candidate_EvaluationSerializer(candidate_Evaluations)
        return Response({'Message': 'Success', 'data': serializer_class.data})
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
        return Response({"Message":"Success","data":Job_Description_Documents})

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
# Data Udation based on the given requierment of the primary key
    def put(self, request):
        queryset = Job_Description_Document.objects.get(job_description_id=request.data['job_description_id'])
        serializer = jobDiscriptionSerializer(queryset, data= request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HHTP_404_NOT_FOUND)

# API used to retrive User Detail Using User Id Only
class JobDiscriptiondetailView(APIView):
    
    def get(self,request,Job_Description_Documents):
        Job_Description_Documents=Job_Description_Document.objects.get(job_description_id=Job_Description_Documents)
        serializer_class=jobDiscriptionSerializer(Job_Description_Documents)
        return Response({'Message': 'Success', 'data': serializer_class.data})


@api_view(['GET'])
def get_applicant_score(request):
    job_id = request.query_params.get('job_id', None)
    if job_id is not None:
        job = Job.objects.all().filter(job_id=job_id)
        job_ser = JobSerializer(job, many=True)
        job_file = job_ser.data[0]['file']
        # job_file_ext = os.path.splitext(job_file.name)[-1].lower()
        applications_querysets = Application.objects.all().filter(job=job_id)
        applications = ApplicationSerializer(applications_querysets, many=True)
        # return Response({'Message': 'Success', 'data': applications.data})
        # loop fore each application
        candidate_evaluations = []
        for application in applications.data:
            try:
                user_id = application['user']
                applicant_document_q = Applicant_Document.objects.all().filter(user=user_id)
                applicant_doc = ApplicatDocumentSerializer(applicant_document_q, many=True)
                user_file = applicant_doc.data[0]['document']
                # user_file_ext = os.path.splitext(user_file.name)[-1].lower()
                job_file_path = settings.BASE_DIR + job_file
                print('base directory' + settings.BASE_DIR)
                
                user_file_path = settings.BASE_DIR + user_file

                print(job_file_path, user_file_path)

                print('user_file: ' + user_file_path)
                print('job_file: ' + job_file_path)
                #return Response({'jobfile': job_file_path, 'userfile': user_file_path}
                resume_s = extract_text(user_file_path)
                print(resume_s)
                jobdesc = extract_text(job_file_path)
                score_r = score(resume_s, jobdesc)
                evaluation_result = score_r

                candidate = candidate_Evaluation()
                #candidate.candidate_evaluation_id = 0
                candidate.evaluation_notes = ''
                candidate.job_id = job_id
                candidate.evaluation_result=evaluation_result
                candidate.applicant_id = user_id
                user_obj = user.objects.get(pk=user_id)

                candidate.applicant = user_obj

                job_obj = Job.objects.get(pk=job_id)
                candidate.job = job_obj

                candidate_evaluations.append(candidate)
                candidate_ser = candidate_EvaluationSerializer(data=candidate)
                #if candidate.is_valid():
                try:
                    candidate.save()
                    print('Saving success')
                except Exception as e:
                    print(e)
                    continue
                    #print(candidate_ser.errors)
                #return Response({'jobfile': job_file_path, 'userfile': user_file_path})
            except Exception as e:
                print('score error')
                print(e)
                continue
            return Response({'Message': 'Success',
                 'data': candidate_EvaluationSerializer(candidate_evaluations, many=True).data})
    else:
        return Response({'Error': 'No job id is provided'})