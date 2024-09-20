from django.db import models
from django.utils import timezone

# Create your models here.
class Opportunities(models.Model):

    Nmae=models.CharField(max_length=100)
    cc=models.BigIntegerField()
    contact_no=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    fee_coated=models.DecimalField(max_digits=12,decimal_places=2,default=0.0)
    description=models.CharField(max_length=200,default="N/A")
    datetime=models.DateTimeField(time=timezone.now)

    LEAD_STATUS_CHOICES=[
        ("Not contacted","Not contacted"),
        ("Attempted","Attempted"),
        ("warm lead","warm lead"),
        ("cold lead","cold lead"),
    ]

    LEAD_SOURCE_CHOICES = [
        ('None', 'None'),
        ('WalkIn', 'WalkIn'),
        ('StudentReferral', 'StudentReferral'),
        ('Demo', 'Demo'),
        ('WebSite', 'WebSite'),
        ('WebsiteChat', 'WebsiteChat'),
        ('InboundCall', 'InboundCall'),
        ('GoogleAdWords', 'GoogleAdWords'),
        ('FacebookAds', 'FacebookAds'),
        ('GoogleMyBusiness', 'GoogleMyBusiness'),
        ('WhatsAppDigitalLync', 'WhatsAppDigitalLync'),
    ]

    
    STACK_CHOICES = [
      ("Life Skills","Life Skills"),
      ("Study Abroad","Study Abroad"),
      ("HR","HR"),
    ]

    CLASS_MODE_CHOICES = [
        ('HYD ClassRoom', 'HYD ClassRoom'),
        ('BLR ClassRoom', 'BLR ClassRoom'),
        ('India Online', 'India Online'),
        ('International Online', 'International Online'),
    ]

    COURSES_CHOICES = [
        ('Angulaar', 'Angulaar'),
        ('AWS', 'AWS'),
        ('AWSWithDevOps', 'AWSWithDevOps'),
        ('Azure', 'Azure'),
        ('AzureDevOps', 'AzureDevOps'),
        ('BusinessAnlayst', 'BusinessAnlayst'),
        ('CloudOpsMasters', 'CloudOpsMasters'),
        ('DevOps', 'DevOps'),
        ('FrontEndAngular', 'FrontEndAngular'),
        ('FrontEndReact', 'FrontEndReact'),
        ('FullStackJAVA', 'FullStackJAVA'),
        ('FullStackMEAN', 'FullStackMEAN'),
        ('FullStackMERN', 'FullStackMERN'),
        ('FullstackPython', 'FullstackPython'),
        ('FullStackReactJAVA', 'FullStackReactJAVA'),
        ('Java', 'Java'),
        ('NeedCounselling', 'NeedCounselling'),
        ('Others', 'Others'),
        ('PowerBI', 'PowerBI'),
        ('Python', 'Python'),
        ('React', 'React'),
        ('SalesForceAdmin', 'SalesForceAdmin'),
        ('SalesforceDeveloper', 'SalesforceDeveloper'),
        ('ServiceNow', 'ServiceNow'),
        ('AzureDataEngineer', 'AzureDataEngineer'),
        ('Tableau', 'Tableau'),
        ('Testing', 'Testing'),
    ]


    lead_source=models.CharField(
        max_length=20,
        choices= LEAD_SOURCE_CHOICES ,
        default="None",
    )

    class_mode=models.CharField(
        max_length=20,
        choices= CLASS_MODE_CHOICES,
        default="HYDclassrrom",
    )

    lead_status=models.CharField(
        max_length=20,
        choices= LEAD_STATUS_CHOICES,
        default="None",
    )

    courses=models.CharField(
        max_length=20,
        choices= COURSES_CHOICES,
        default="None",
    )

    stack=models.CharField(
        max_length=20,
        choices=TECH_STACK_CHOICES ,
        default="None",
    )
