# Generated by Django 4.0.5 on 2022-06-27 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATS_APP', '0002_alter_applicant_document_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill_set',
            name='skill_level',
        ),
    ]