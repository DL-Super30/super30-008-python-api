from django.db import models
# from django.utils import timezone


# Create your models here.
class opportunities(models.Model):

    BATCH_TIMING_CHOICES = [
        ('7AM_8AM', '7AM_8AM'),
        ('8AM_9AM', '8AM_9AM'),
        ('9AM_10AM', '9AM_10AM'),
        ('10AM_11AM', '10AM_11AM'),
        ('11AM_12PM', '11AM_12PM'),
        ('12PM_1PM', '12PM_1PM'),
        ('1PM_2PM', '1PM_2PM'),
        ('2PM_3PM', '2PM_3PM'),
        ('3PM_4PM', '3PM_4PM'),
        ('4PM_5PM', '4PM_5PM'),
        ('5PM_6PM', '5PM_6PM'),
        ('6PM_7PM', '6PM_7PM'),
        ('7PM_8PM', '7PM_8PM'),
        ('8PM_9PM', '8PM_9PM'),
    ]
    LEAD_STATUS_CHOICES = [
        ('Not Contacted','Not Contacted'),
        ('Attempted','Attempted'),
        ('Warm Lead','Warm Lead'),
        ('Cold Lead','Cold Lead'),
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
        ('WhatsAppSkillCapital', 'WhatsAppSkillCapital'),
        
    ]
    TECH_STACK_CHOICES = [
        ('Life Skills','Life Skills'),
        ('Study Abroad','Study Abroad'),
        ('HR','HR'),
    ]

    COURSES_CHOICES = [
        ('HR Business Partner','HR Business Partner'),
        ('HR Generalist Core HR','HR Generalist Core HR'),
        ('HR Analytics','HR Analytics'),
        ('Spoken English','Spoken English'),
        ('Public Speaking','Public Speaking'),
        ('Communication Skills','Communication Skills'),
        ('Soft Skills','Soft Skills'),
        ('Personality Development','Personality Development'),
        ('Aptitude','Aptitude'),
        ('IELTS','IELTS'),
        ('TOEFL','TOEFL'),
        ('PTE','PTE'),
        ('GRE','GRE'),
        ('GMAT','GMAT'),
        ('Recruitment Specialist','Recruitment Specialist'),
        ('Payroll Specialist','Payroll Specialist'),
        ('Learning and Development','Learning and Development'),
        ('Others','Others'),
        ('Finance','Finance'),
        ('Competitive Exams','Competitive Exams'),
        ('HR Manage','HR Manage'),
    ]
    
    CLASS_MODE_CHOICES = [
        ('International Online','International Online'),
        ('India Online','India Online'),
        ('BLR Classroom','BLR Classroom'),
        ('HYD Classroom','Hyd Classroom'),
    ]
    OPPORTUNITY_STATUS = [
        ('Visiting','Visiting'),
        ('Visited','Visited'),
        ('Demo Attended','Demo Attended'),
        ('Lost Opportunity','Lost Opportunity'),
    ]
    OPPORTUNITY_STAGE =[
        ('None','None'),
        ('Advanced Discussion','Advanced Discussion'),
        ('Ready To Join','Ready To Join'),
        ('Call Not Answered','Call Not Answered'),
        ('Visiting','Visiting'),
        ('Fees Negotiation','Fees Negotiation'),
        ('Batch Allocation','Batch Allocation'),
        ('Need Time This Week','Need Time This Week'),
        ('Need Time Next Week','Need Time Next Week'),
        ('Need Time This Month','Need Time This Month'),
        ('Need Time Next Month','Need Time Next Month'),
        ('Special Requirements ','Special Requirements '),
        ('Closed Own (Register) ','Closed Own (Register) '),
        ('Busy & Asked a Call Back ','Busy & Asked a Call Back' ),
        ('Closed Lost','Closed Lost')
        ]
    DEMOATTENDED_STAGE=[
        ('None','None'),
        ('Ready To Join','Ready To Join'),
        ('Advanced Discussion','Advanced Discussion'),
        ('Call Not Answered','Call Not Answered'),
        ('Visiting','Visiting'),
        ('Fees Negotiation','Fees Negotiation'),
        ('Batch Allocation','Batch Allocation'),
        ('Need Time This Week','Need Time This Week'),
        ('Need Time Next Week','Need Time Next Week'),
        ('Need Time This Month','Need Time This Month'),
        ('Need Time Next Month','Need Time Next Month'),
        ('Special Requirements ','Special Requirements '),
        ('Closed Own (Register) ','Closed Own (Register) '),
        ('Closed Lost (Cold Lead) ','Closed Lost (Cold Lead) '),
        ]
    VISITED_STAGE=[
        ('None','None'),
        ('Call Not Answered','Call Not Answered'),
        ('Ready To Join','Ready To Join'),
        ('Fees Negotiation','Fees Negotiation'),
        ('Batch Allocation','Batch Allocation'),
        ('Intrested Demo','Intrested Demo'),
        ('Special Requirements ','Special Requirements '),
        ('Need Time This Week','Need Time This Week'),
        ('Need Time Next Week','Need Time Next Week'),
        ('Need Time This Month','Need Time This Month'),
        ('Need Time Next Month','Need Time Next Month'),
        ('Closed Own (Register) ','Closed Own (Register) '),
        ('Closed Lost (Cold Lead) ','Closed Lost (Cold Lead) '),
        ]
    LOSTOPPORTUNITY_REASON=[
        ('None','None'),
        ('Invalid Number','Invalid Number'),
        ('Not Intersted','Not Intersted'),
        ('Joined Other Institute','Joined Other Institute'),
        ('Asking Free Course','Asking Free Course'),
        ('Pay After Placement','Pay After Placement'),

    ]
    

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cc = models.BigIntegerField()
    contact_no = models.BigIntegerField()
    email = models.EmailField(max_length=255)
    fee_coated = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField() 
   

    

 

    batch_timing = models.CharField(
        max_length=10,  # Adjusted max_length to fit the longest value
        choices=BATCH_TIMING_CHOICES,
        default='7AM_8AM',
    )
    lead_status = models.CharField(
        max_length=13,
        choices=LEAD_STATUS_CHOICES,
        default='None',
    )
    lead_source = models.CharField(
        max_length=24,
        choices=LEAD_SOURCE_CHOICES,
        default='None',
    )

  
    TechStack= models.CharField(
        max_length=24,
        choices=TECH_STACK_CHOICES,
        default='Select Stack',
    )
    Course = models.CharField(
        max_length=24,
        choices=COURSES_CHOICES,
        default='None',
    )
    class_mode = models.CharField(
        max_length=24,
        choices=CLASS_MODE_CHOICES,
        default='HYDClassRoom',
    )
    opportunity_status = models.CharField(
        max_length=30,
        choices=OPPORTUNITY_STATUS,
        default='Select Opportunity Status',
    )
    opportunity_stage = models.CharField(
        max_length=30,
        choices=OPPORTUNITY_STAGE,
        default='Select Opportunity Stage',
    )
    demoattended_stage = models.CharField(
        max_length=30,
        choices=DEMOATTENDED_STAGE,
        default='Select Demo Attend Stage',
    )
    visited_stage = models.CharField(
        max_length=30,
        choices=VISITED_STAGE,
        default='Select Visited Stage',
    )
    lostopportunity_reason = models.CharField(
        max_length=30,
        choices=LOSTOPPORTUNITY_REASON,
        default='Select Lost Opportunity Reason',
    )




      



 

 