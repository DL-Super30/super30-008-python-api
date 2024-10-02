from django.db import models
# from django.utils import timezone


# Create your models here.
class opportunities(models.Model):

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
    TECH_STACK_CHOICES = [
        ('Life Skills', 'Life Skills'),
        ('Study Abroad', 'Study Abroad'),
        ('HR', 'HR')

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
    OPPORTUNITY_STATUS = [
        ('Visiting', 'Visiting'),
        ('Visited', 'Visited'),
        ('Demo Attended', 'Demo Attended'),
        ('Lost Opportunity', 'Lost Opportunity')


    ]
    OPPORTUNITY_STAGE =[
        ('None', 'None'),
        ('Advanced Discussion', 'Advanced Discussion'),
        ('Ready To Join', 'Ready To Join'),
        ('Call Not Answered', 'Call Not Answered'),
        ('Visiting', 'Visiting'),
        ('Fees Negotiation', 'Fees Negotiation'),
        ('Batch Allocation', 'Batch Allocation'),
        ('Need Time This Week', 'Need Time This Week'),
        ('Need Time Next Week', 'Need Time Next Week'),
        ('Need Time This Month', 'Need Time This Month'),
        ('Need Time Next Month', 'Need Time Next Month'),
        ('Special Requirements', 'Special Requirements'),
        ('Closed Own Register', 'Closed Own Register'),
        ('Busy Asked A Call Back', 'Busy Asked A Call Back'),
        ('Closed Lost', 'Closed Lost')


        ]
    DEMOATTENDED_STAGE=[
        ('None', 'None'),
        ('Ready To Join', 'Ready To Join'),
        ('Advanced Discussion', 'Advanced Discussion'),
        ('Call Not Answered', 'Call Not Answered'),
        ('Visiting', 'Visiting'),
        ('Fees Negotiation', 'Fees Negotiation'),
        ('Batch Allocation', 'Batch Allocation'),
        ('Need Time This Week', 'Need Time This Week'),
        ('Need Time Next Week', 'Need Time Next Week'),
        ('Need Time This Month', 'Need Time This Month'),
        ('Need Time Next Month', 'Need Time Next Month'),
        ('Special Requirements', 'Special Requirements'),
        ('Closed Own Register', 'Closed Own Register'),
        ('Closed Lost Cold Lead', 'Closed Lost Cold Lead')


        ]
    VISITED_STAGE=[
        ('None', 'None'),
        ('Call Not Answered', 'Call Not Answered'),
        ('Ready To Join', 'Ready To Join'),
        ('Fees Negotiation', 'Fees Negotiation'),
        ('Batch Allocation', 'Batch Allocation'),
        ('Interested Demo', 'Interested Demo'),
        ('Special Requirements', 'Special Requirements'),
        ('Need Time This Week', 'Need Time This Week'),
        ('Need Time Next Week', 'Need Time Next Week'),
        ('Need Time This Month', 'Need Time This Month'),
        ('Need Time Next Month', 'Need Time Next Month'),
        ('Closed Own Register', 'Closed Own Register'),
        ('Closed Lost Cold Lead', 'Closed Lost Cold Lead')


        ]
    LOSTOPPORTUNITY_REASON=[
        ('None', 'None'),
        ('Invalid Number', 'Invalid Number'),
        ('Not Interested', 'Not Interested'),
        ('Joined Other Institute', 'Joined Other Institute'),
        ('Asking Free Course', 'Asking Free Course'),
        ('Pay After Placement', 'Pay After Placement')

    ]
    

    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    CC = models.BigIntegerField()
    Contact_No = models.BigIntegerField()
    Email = models.EmailField(max_length=255)
    Fee_Coated = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField()
    Date = models.DateField() 
   
    Batch_Timing = models.CharField(
        max_length=10,  # Adjusted max_length to fit the longest value
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
        default='None',
    )
    Class_Mode = models.CharField(
        max_length=24,
        choices=CLASS_MODE_CHOICES,
        default='HYD Classroom',
    )
    Opportunity_Status = models.CharField(
        max_length=30,
        choices=OPPORTUNITY_STATUS,
        default='Visited',
    )
    Opportunity_Stage = models.CharField(
        max_length=30,
        choices=OPPORTUNITY_STAGE,
        default='None',
    )
    Demoattended_Stage = models.CharField(
        max_length=30,
        choices=DEMOATTENDED_STAGE,
        default='None',
    )
    Visited_Stage = models.CharField(
        max_length=30,
        choices=VISITED_STAGE,
        default='None',
    )
    Lost_Opportunity_Reason = models.CharField(
        max_length=30,
        choices=LOSTOPPORTUNITY_REASON,
        default='Not Interested',
    )




      



 

 