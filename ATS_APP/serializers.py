from cProfile import label
from typing import ItemsView
from rest_framework import serializers

from ATS_APP.models import user
from ATS_APP.models import Applicant_Document, Application, Company, Education, Experience, Job, Job_Description_Document, Role, Skill_Set, User_Role, applicant_cv, candidate_Evaluation, job_category, job_platforms

class UserSerializer(serializers.Serializer):
    #id = serializers.IntegerField(label="User ID:")
    first_name = serializers.CharField(label="First Name:")
    middle_name=serializers.CharField(label="Middle Name:")
    last_name = serializers.CharField(label="Last Name:")
    email = serializers.CharField(label="Email:")
    password = serializers.CharField(label="Password:")
    city=serializers.CharField(label="City:")
    phone=serializers.CharField(label="Phone:")
    country=serializers.CharField(label="Country:")

class userdetailSerializer(serializers.ModelSerializer):


    class Meta:
        model = user
        fields = ('user_id','first_name', 'middle_name','last_name','email','password','city','phone','Country')
        field='__all__'

# User Role Serializer Starts Here

class UserRoleSerializer(serializers.Serializer):
    role = serializers.CharField(label="Role:")
    user=serializers.CharField(label="User:")

class UserRoleSerializer(serializers.ModelSerializer):


    class Meta:
        model = User_Role
        fields = ('role', 'user',)

# Role Serializer Starts Here

class RoleSerializer(serializers.Serializer):
    name=serializers.CharField(label="Name:")

class RoleSerializer(serializers.ModelSerializer):


    class Meta:
        model = Role
        fields = ('role_id','name')

#  Skill Set Starts Here

class SkillsetSerializer(serializers.Serializer):
    skill = serializers.CharField(label="skill:")
    skill_level=serializers.CharField(label="skill_level:")
    applicant_cv=serializers.CharField(label="applicant_cv:")

class SkillsetSerializer(serializers.ModelSerializer):


    class Meta:
        model = Skill_Set
        fields = ('skill','skill_level','applicant_cv')

# Job Platform Starts Here

class jobplatformSerializer(serializers.Serializer):
    code = serializers.CharField(label="code:")
    name=serializers.CharField(label="name:")
    description=serializers.CharField(label="description:")

class jobplatformSerializer(serializers.ModelSerializer):


    class Meta:
        model = job_platforms
        fields = ('code','name','description')

#  Company Starts Here

class CompanySerializer(serializers.Serializer):
    code = serializers.CharField(label="code:")
    name=serializers.CharField(label="name:")
    description=serializers.CharField(label="description:")

class CompanySerializer(serializers.ModelSerializer):


    class Meta:
        model = Company
        fields = ('code','name','description')

#  applicant_cv Starts Here

class Applicant_cvSerializer(serializers.Serializer):
    #applicant_id = serializers.(label="date_created:")
    date_created=serializers.DateTimeField(label="gender:")
    gender=serializers.CharField(label="zip_code:")
    summary = serializers.CharField(label="country:")
    last_updated=serializers.DateTimeField(label="city:")
    zip_code=serializers.CharField(label="phone:")
    country=serializers.CharField(label="phone2:")
    city=serializers.CharField(label="zip_code:")
    phone = serializers.CharField(label="training_certification:")
    phone2=serializers.CharField(label="applicant_cv:")
    training_certification = serializers.CharField(label="training_certification:")
    applicant_cv=serializers.FileField(label="applicant_cv:")

class Applicant_cvSerializer(serializers.ModelSerializer):
 

    class Meta:
        model = applicant_cv
        fields = '__all__'

# Experiance Starts Here

class ExperianceSerializer(serializers.Serializer):
    organization = serializers.CharField(label="organization:")
    title=serializers.CharField(label="title:")
    begin_date=serializers.DateTimeField(label="begin_date:")
    end_date = serializers.DateTimeField(label="end_date:")
    applicant_cv=serializers.CharField(label="applicant_cv:")

class ExperianceSerializer(serializers.ModelSerializer):


    class Meta:
        model = Experience
        fields = ('organization','title','begin_date','end_date','applicant_cv')
        

#  Education Starts Here

class EducationSerializer(serializers.Serializer):
    institution_name = serializers.CharField(label="institution_name:")
    degree_obtained=serializers.DateTimeField(label="degree_obtained:")
    date_attended_from=serializers.DateTimeField(label="date_attended_from:")
    date_attended_to = serializers.DateTimeField(label="date_attended_to:")
    applicant_cv=serializers.CharField(label="applicant_cv:")

class EducationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Education
        fields = ('institution_name','degree_obtained','date_attended_from','date_attended_to','applicant_cv')


# Job Starts Here

class JobSerializer(serializers.Serializer):
    description = serializers.CharField(label="description:")
    date_published=serializers.DateTimeField(label="date_published:")
    job_deadline=serializers.DateTimeField(label="job_deadline:")
    number_of_vacancies = serializers.CharField(label="number_of_vacancies:")
    job_category=serializers.CharField(label="job_category:")
    job_position = serializers.CharField(label="job_position:")
    job_platform=serializers.CharField(label="job_platform:")
    organization_name=serializers.CharField(label="organization_name:")
    file = serializers.FileField(label="file:")
   
class JobSerializer(serializers.ModelSerializer):


    class Meta:
        model = Job
        fields = ('description','date_published','job_deadline','number_of_vacancies','job_category','job_position','job_platform','organization_name','file')


# JobCategory Starts Here

class JobcategorySerializer(serializers.Serializer):
     
    code=serializers.CharField(label="code:")
    name=serializers.CharField(label="name:")
    description = serializers.CharField(label="description:")
  

   
class JobcategorySerializer(serializers.ModelSerializer):
 

    class Meta:
        model = job_category
        fields = ('code','name','description')


# Application Starts Here

class ApplicationSerializer(serializers.Serializer):
     
    date_of_application=serializers.DateTimeField(label="Date_of_Application:")
    job=serializers.CharField(label="job:")
    user = serializers.CharField(label="User:")
    application_status = serializers.CharField(label="Application_Status:")
  
  
class ApplicationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Application
        fields = '__all__'


# Applicant_Document Starts Here

class ApplicatDocumentSerializer(serializers.Serializer):
    name=serializers.CharField(label="Name:")
    document=serializers.FileField(label="Document:")
    url = serializers.CharField(label="URL:")
    last_updated = serializers.FileField(label="Last_Updated:")
    user = serializers.CharField(label="User:")
  

   
class ApplicatDocumentSerializer(serializers.ModelSerializer):
    #tag = ApplicatDocumentSerializer()

    class Meta:
        model = Applicant_Document
        fields = ('applicant_document_id','name','document','url','last_updated','user')
        fields='__all__'


# candidate_Evaluation Starts Here

class candidate_EvaluationSerializer(serializers.Serializer):
     
    evaluation_notes=serializers.CharField(label="evaluation_notes:")
    job=serializers.CharField(label="job:")
    applicant = serializers.CharField(label="applicant:")
    evaluation_result = serializers.CharField(label="evaluation_result:")
  

   
class candidate_EvaluationSerializer(serializers.ModelSerializer):
 

    class Meta:
        model = candidate_Evaluation
        fields = ('evaluation_notes','job','applicant','evaluation_result')


# Job_Discription Starts Here

class jobDiscriptionSerializer(serializers.Serializer):
     
    name=serializers.CharField(label="name:")
    document=serializers.FileField(label="document:")
    last_updated = serializers.DateTimeField(label="last_updated:")
    job = serializers.CharField(label="job:")
  

   
class jobDiscriptionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Job_Description_Document
        fields = ('name','document','last_updated','job')



