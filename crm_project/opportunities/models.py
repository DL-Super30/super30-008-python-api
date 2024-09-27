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
        ('notContacted', 'notContacted'),
        ('attempted', 'attempted'),
        ('warmLead', 'warmLead'),
        ('coldLead', 'coldLead')
       
    ]

    LEAD_SOURCE_CHOICES = [
        ('none', 'none'),
        ('walkIn', 'walkIn'),
        ('studentReferral', 'studentReferral'),
        ('demo', 'demo'),
        ('webSite', 'webSite'),
        ('webSiteChat', 'webSiteChat'),
        ('inboundCall', 'inboundCall'),
        ('googleAdWords', 'googleAdWords'),
        ('facebookAds', 'facebookAds'),
        ('googleMyBusiness', 'googleMyBusiness'),
        ('whatsAppSkillCapital', 'whatsAppSkillCapital')
        
    ]
    TECH_STACK_CHOICES = [
        ('lifeSkills', 'lifeSkills'),
        ('studyAbroad', 'studyAbroad'),
        ('hr', 'hr')
    ]

    COURSES_CHOICES = [
        ('hrBusinessPartner', 'hrBusinessPartner'),
        ('hrGeneralistCoreHR', 'hrGeneralistCoreHR'),
        ('hrAnalytics', 'hrAnalytics'),
        ('spokenEnglish', 'spokenEnglish'),
        ('publicSpeaking', 'publicSpeaking'),
        ('communicationSkills', 'communicationSkills'),
        ('softSkills', 'softSkills'),
        ('personalityDevelopment', 'personalityDevelopment'),
        ('aptitude', 'aptitude'),
        ('ielts', 'ielts'),
        ('toefl', 'toefl'),
        ('pte', 'pte'),
        ('gre', 'gre'),
        ('gmat', 'gmat'),
        ('recruitmentSpecialist', 'recruitmentSpecialist'),
        ('payrollSpecialist', 'payrollSpecialist'),
        ('learningAndDevelopment', 'learningAndDevelopment'),
        ('others', 'others'),
        ('finance', 'finance'),
        ('competitiveExams', 'competitiveExams'),
        ('hrManage', 'hrManage')

    ]
    
    CLASS_MODE_CHOICES = [
        ('internationalOnline', 'internationalOnline'),
        ('indiaOnline', 'indiaOnline'),
        ('blrClassroom', 'blrClassroom'),
        ('hydClassroom', 'hydClassroom')
    ]
    OPPORTUNITY_STATUS = [
        ('visiting', 'visiting'),
        ('visited', 'visited'),
        ('demoAttended', 'demoAttended'),
        ('lostOpportunity', 'lostOpportunity')

    ]
    OPPORTUNITY_STAGE =[
        ('none', 'none'),
        ('advancedDiscussion', 'advancedDiscussion'),
        ('readyToJoin', 'readyToJoin'),
        ('callNotAnswered', 'callNotAnswered'),
        ('visiting', 'visiting'),
        ('feesNegotiation', 'feesNegotiation'),
        ('batchAllocation', 'batchAllocation'),
        ('needTimeThisWeek', 'needTimeThisWeek'),
        ('needTimeNextWeek', 'needTimeNextWeek'),
        ('needTimeThisMonth', 'needTimeThisMonth'),
        ('needTimeNextMonth', 'needTimeNextMonth'),
        ('specialRequirements', 'specialRequirements'),
        ('closedOwnRegister', 'closedOwnRegister'),
        ('busyAskedACallBack', 'busyAskedACallBack'),
        ('closedLost', 'closedLost')

        ]
    DEMOATTENDED_STAGE=[
        ('none', 'none'),
        ('readyToJoin', 'readyToJoin'),
        ('advancedDiscussion', 'advancedDiscussion'),
        ('callNotAnswered', 'callNotAnswered'),
        ('visiting', 'visiting'),
        ('feesNegotiation', 'feesNegotiation'),
        ('batchAllocation', 'batchAllocation'),
        ('needTimeThisWeek', 'needTimeThisWeek'),
        ('needTimeNextWeek', 'needTimeNextWeek'),
        ('needTimeThisMonth', 'needTimeThisMonth'),
        ('needTimeNextMonth', 'needTimeNextMonth'),
        ('specialRequirements', 'specialRequirements'),
        ('closedOwnRegister', 'closedOwnRegister'),
        ('closedLostColdLead', 'closedLostColdLead')

        ]
    VISITED_STAGE=[
        ('none', 'none'),
        ('callNotAnswered', 'callNotAnswered'),
        ('readyToJoin', 'readyToJoin'),
        ('feesNegotiation', 'feesNegotiation'),
        ('batchAllocation', 'batchAllocation'),
        ('interestedDemo', 'interestedDemo'),
        ('specialRequirements', 'specialRequirements'),
        ('needTimeThisWeek', 'needTimeThisWeek'),
        ('needTimeNextWeek', 'needTimeNextWeek'),
        ('needTimeThisMonth', 'needTimeThisMonth'),
        ('needTimeNextMonth', 'needTimeNextMonth'),
        ('closedOwnRegister', 'closedOwnRegister'),
        ('closedLostColdLead', 'closedLostColdLead')

        ]
    LOSTOPPORTUNITY_REASON=[
        ('none', 'none'),
        ('invalidNumber', 'invalidNumber'),
        ('notInterested', 'notInterested'),
        ('joinedOtherInstitute', 'joinedOtherInstitute'),
        ('askingFreeCourse', 'askingFreeCourse'),
        ('payAfterPlacement', 'payAfterPlacement')

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




      



 

 