from django.db import models
from django.utils import timezone

# Create your models here.
class leads(models.Model):

    user_name=models.CharField(max_length=100)
    contact_no=models.BigIntegerField()
    cc=models.BigIntegerField(default=+91)
    email=models.EmailField(default="N/A")
    fee_coated=models.DecimalField(max_digits=12,decimal_places=2,default=0.0)
    datefield=models.DateTimeField(default=timezone.now)
    description=models.TextField(max_length=300,default="N/A")

    LEAD_STATUS_CHOICES=[
        ("None","None"),
        ("Not contacted","Not contacted"),
        ("Attempted","Attempted"),
        ("warm lead","warm lead"),
        ("opportunity","opportunity"),
        ("attendedemo","attendedemo"),
        ("visited","visited"),
        ("registered","registered"),
        ("coldlead","coldlead"),
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

    
    TECH_STACK_CHOICES = [
        ('CloudOps', 'CloudOps'),
        ('Salesforce', 'Salesforce'),
        ('FullStack', 'FullStack'),
        ('DataStack', 'DataStack'),
        ('ServiceNow', 'ServiceNow'),
        ('BusinessStack', 'BusinessStack'),
        ('CareerCounselling', 'CareerCounselling'),
    ]

    CLASS_MODE_CHOICES = [
        ('HYDClassRoom', 'HYDClassRoom'),
        ('BLRClassRoom', 'BLRClassRoom'),
        ('IndiaOnline', 'IndiaOnline'),
        ('InternationalOnline', 'InternationalOnline'),
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

    tech_stack=models.CharField(
        max_length=20,
        choices=TECH_STACK_CHOICES ,
        default="None",
    )

    