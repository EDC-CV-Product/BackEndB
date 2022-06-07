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
        user=user.objects.all().values()
        # can also write in one of the following options
        #return Response(serializers.data)
        return Response({"Message":"List of Users","User List":user})

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
        user=user.objects.filter(user_id=uid)
        serializer_class=UserSerializer(user,many=True)
        return Response(serializer_class.data)

# API for User Role Starts Here

class UserRoleApiView(APIView):
    serializer_class=UserRoleSerializer
    def get(self,request):
        User_Role=User_Role.objects.all().values()
        return Response({"Message":"List of User roles","User Role List":User_Role})

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
        User_Role=User_Role.objects.filter(user_role_id=urroleid)
        serializer_class=UserRoleSerializer(User_Role,many=True)
        return Response(serializer_class.data)

# API for  Role Starts Here

class RoleApiView(APIView):
    serializer_class=RoleSerializer
    def get(self,request):
        Role=Role.objects.all().values()
        return Response({"Message":"List of User roles"," Role List":Role})

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
        Role=Role.objects.filter(role_id=roo)
        serializer_class=RoleSerializer(Role,many=True)
        return Response(serializer_class.data)

# API for  Skill Set Starts Here

class SkillsetApiView(APIView):
    serializer_class=SkillsetSerializer
    def get(self,request):
        Skill_Set=Skill_Set.objects.all().values()
        return Response({"Message":"List of User roles","User Role List":Skill_Set})

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
        Skill_Set=Skill_Set.objects.filter(skill_set_id=skill_det)
        serializer_class=SkillsetSerializer(Skill_Set,many=True)
        return Response(serializer_class.data)

# API for  Job Platform Starts Here

class JobPlatformApiView(APIView):
    serializer_class=jobplatformSerializer
    def get(self,request):
        job_platforms=job_platforms.objects.all().values()
        return Response({"Message":"List of Job Platforms","Job Platform List":job_platforms})

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
        Company=Company.objects.all().values()
        return Response({"Message":"List of companey","companey List":Company})

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
        Company=Company.objects.filter(companey_id=urid)
        serializer_class=CompanySerializer(Company,many=True)
        return Response(serializer_class.data)


# API for  applicant_cv Starts Here

class applicant_cvApiView(APIView):
    serializer_class=Applicant_cvSerializer
    def get(self,request):
        applicant_cv=applicant_cv.objects.all().values()
        return Response({"Message":"List of applicant cv","applicant cv List":applicant_cv})

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
        applicant_cv=applicant_cv.objects.filter(applicant_id=urid)
        serializer_class=Applicant_cvSerializer(applicant_cv,many=True)
        return Response(serializer_class.data)


# API for  Experiance Starts Here

class ExperianceApiView(APIView):
    serializer_class=ExperianceSerializer
    def get(self,request):
        Experience=Experience.objects.all().values()
        return Response({"Message":"List of Job Platforms","Job Platform List":Experience})

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
        Experience=Experience.objects.filter(experiance_id=urid)
        serializer_class=ExperianceSerializer(Experience,many=True)
        return Response(serializer_class.data)


# API for  Education Starts Here

class EducationApiView(APIView):
    serializer_class=EducationSerializer
    def get(self,request):
        Education=Education.objects.all().values()
        return Response({"Message":"List of Job Platforms","Job Platform List":Education})

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
        Education=Education.objects.filter(education_id=urid)
        serializer_class=EducationSerializer(Education,many=True)
        return Response(serializer_class.data)


# API for  Job Starts Here

class JobApiView(APIView):
    serializer_class=JobSerializer
    def get(self,request):
        Job=Job.objects.all().values()
        return Response({"Message":"List of Job ","Job  List":Job})

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
        Job=Job.objects.filter(job_id=jobid)
        serializer_class=JobSerializer(Job,many=True)
        return Response(serializer_class.data)

# API for  job_category Starts Here

class JobCategoryApiView(APIView):
    serializer_class=JobcategorySerializer
    def get(self,request):
        job_category=job_category.objects.all().values()
        return Response({"Message":"List of job catagory ","Job category":job_category})

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
        job_category=job_category.objects.filter(job_category_id=urid)
        serializer_class=JobcategorySerializer(job_category,many=True)
        return Response(serializer_class.data)

# API for  Application Starts Here

class ApplicationApiView(APIView):
    serializer_class=ApplicationSerializer
    def get(self,request):
        Application=Application.objects.all().values()
        return Response({"Message":"List of Application ","Application":Application})

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
        Application=Application.objects.filter(application_id=App)
        serializer_class=ApplicationSerializer(Application,many=True)
        return Response(serializer_class.data)

# API for  Applicant_Document Starts Here

class Applicant_DocumentApiView(APIView):
    serializer_class=ApplicatDocumentSerializer
    def get(self,request):
        Applicant_Document=Applicant_Document.objects.all().values()
        return Response({"Message":"List of Applicant_Document ","Applicant_Document":Applicant_Document})

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
        Applicant_Document=Applicant_Document.objects.filter(user_id=appid)
        serializer_class=ApplicatDocumentSerializer(Applicant_Document,many=True)
        return Response(serializer_class.data)

# API for  candidate_Evaluation Starts Here

class Candidate_EvaluationApiView(APIView):
    serializer_class=candidate_EvaluationSerializer
    def get(self,request):
        candidate_Evaluation=candidate_Evaluation.objects.all().values()
        return Response({"Message":"List of Candidate_evaluation ","Candidate_evaluation":candidate_Evaluation})

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
        candidate_Evaluation=candidate_Evaluation.objects.filter(candidate_evaluation_id=urid)
        serializer_class=candidate_EvaluationSerializer(candidate_Evaluation,many=True)
        return Response(serializer_class.data)

# API for  Job_Description_Document Starts Here

class Job_Description_DocumentApiView(APIView):
    serializer_class=jobDiscriptionSerializer
    def get(self,request):
        Job_Description_Document=Job_Description_Document.objects.all().values()
        return Response({"Message":"List of Job_Description_Document ","Job_Description_Document":Job_Description_Document})

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
        Job_Description_Document=Job_Description_Document.objects.filter(job_description_id=urid)
        serializer_class=jobDiscriptionSerializer(Job_Description_Document,many=True)
        return Response(serializer_class.data)
