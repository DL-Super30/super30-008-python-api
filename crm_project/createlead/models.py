from django.db import models
from django.utils import timezone
# import datetime
# import pytz


# Create your models here.
class CreateLeads(models.Model):

    BATCH_TIMING_CHOICES = [
        ('7AM-8AM', '7AM-8AM'),
        ('8AM-9AM', '8AM-9AM'),
        ('9AM-10AM', '9AM-10AM'),
        ('10AM-11AM', '10AM-11AM'),
        ('11AM-12PM', '11AM-12PM'),
        ('12PM-1PM', '12PM-1PM'),
        ('1PM-2PM', '1PM-2PM'),
        ('2PM-3PM', '2PM-3PM'),
        ('3PM-4PM', '3PM-4PM'),
        ('4PM-5PM', '4PM-5PM'),
        ('5PM-6PM', '5PM-6PM'),
        ('6PM-7PM', '6PM-7PM'),
        ('7PM-8PM', '7PM-8PM'),
        ('8PM-9PM', '8PM-9PM')

    ]
    LEAD_STATUS_CHOICES = [
        ('Not Contacted', 'Not Contacted'),
        ('Attempted', 'Attempted'),
        ('Warm Lead', 'Warm Lead'),
        ('Cold Lead', 'Cold Lead')

    ]
    LEAD_SOURCE_CHOICES = [
        ('None', 'None'),
        ('Walk In', 'Walk In'),
        ('Student Referral', 'Student Referral'),
        ('Demo', 'Demo'),
        ('Web Site', 'Web Site'),
        ('Web Site Chat', 'Web Site Chat'),
        ('Inbound Call', 'Inbound Call'),
        ('Google Ad Words', 'Google Ad Words'),
        ('Facebook Ads', 'Facebook Ads'),
        ('Google My Business', 'Google My Business'),
        ('WhatsApp Skill Capital', 'WhatsApp Skill Capital')
    ]

    COURSES_CHOICES = [
        ('HR Business Partner', 'HR Business Partner'),
        ('HR Generalist Core HR', 'HR Generalist Core HR'),
        ('HR Analytics', 'HR Analytics'),
        ('Spoken English', 'Spoken English'),
        ('Public Speaking', 'Public Speaking'),
        ('Communication Skills', 'Communication Skills'),
        ('Soft Skills', 'Soft Skills'),
        ('Personality Development', 'Personality Development'),
        ('Aptitude', 'Aptitude'),
        ('IELTS', 'IELTS'),
        ('TOEFL', 'TOEFL'),
        ('PTE', 'PTE'),
        ('GRE', 'GRE'),
        ('GMAT', 'GMAT'),
        ('Recruitment Specialist', 'Recruitment Specialist'),
        ('Payroll Specialist', 'Payroll Specialist'),
        ('Learning and Development', 'Learning and Development'),
        ('Others', 'Others'),
        ('Finance', 'Finance'),
        ('Competitive Exams', 'Competitive Exams'),
        ('HR Manage', 'HR Manage')

    ]
    CLASS_MODE_CHOICES = [
        ('International Online', 'International Online'),
        ('India Online', 'India Online'),
        ('BLR Classroom', 'BLR Classroom'),
        ('HYD Classroom', 'HYD Classroom')

    ]
    TECH_STACK_CHOICES = [
        ('Life Skills', 'Life Skills'),
        ('Study Abroad', 'Study Abroad'),
        ('HR', 'HR')
    ]

    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    CC = models.BigIntegerField()
    Contact_No = models.BigIntegerField()
    Email = models.EmailField(max_length=255)
    Fee_Coated = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField()
    Date = models.DateField(default=timezone.now)
    
    
    Batch_Timing = models.CharField(
        max_length=10 ,# Adjusted max_length to fit the longest value
        choices=BATCH_TIMING_CHOICES,
        default='7AM-8AM',
    )
    Lead_Status = models.CharField(
        max_length=13,
        choices=LEAD_STATUS_CHOICES,
        default='None',
    )
    Lead_Source = models.CharField(
        max_length=24,
        choices=LEAD_SOURCE_CHOICES,
        default='None',
    )
    Tech_Stack= models.CharField(
        max_length=24,
        choices=TECH_STACK_CHOICES,
        default='HR',
    )
    Course = models.CharField(
        max_length=24,
        choices=COURSES_CHOICES,
        default='PTE',
    )
    Class_Mode = models.CharField(
        max_length=24,
        choices=CLASS_MODE_CHOICES,
        default='HYD Classroom',
    )

