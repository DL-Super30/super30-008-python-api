from django.db import models
from django.utils import timezone

class learners(models.Model):
    FirstName = models.CharField(max_length=225)
    LastName =  models.CharField(max_length=225)
    IdProof = models.CharField(max_length=100)
    Phone = models.BigIntegerField()
    DateofBirth = models.DateField(default=timezone.now)
    Email = models.EmailField(max_length=225)
    RegisteredDate =  models.DateField(default=timezone.now)
    BatchId =  models.CharField(max_length=100)
    Alternatephone = models.BigIntegerField()
    Description =  models.TextField()
    Source = models.CharField()
    LearnerOwner = models.IntegerField()
    Currency = models.DecimalField(max_digits=10, decimal_places=3)
    CounselingDoneBY = models.BooleanField(default=False)
    ExchangeRate = models.DecimalField(max_digits=10, decimal_places=3)
    Leadcratedtime =  models.DateField(default=timezone.now)
    RegisteredCourse = models.IntegerField()
    TechStack = models.CharField(max_length=100)
    CourseComments = models.CharField(max_length=100)
    SlackAccess = models.CharField(max_length=100)
    LMSAccess = models.CharField(max_length=100)
    ModeOfClass = models.CharField(max_length=100)
    Comment = models.CharField(max_length=100)
    PreferableTime=  models.DateField(default=timezone.now)
    BatchTiming = models.DateField(default=timezone.now)

    ATTEND_DEMO_CHOICES=[
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
    LEARNER_STAGE_CHOICES=[
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
        ('closedOwnRegister', 'closedOwnRegister')

    ]
    LOCATION_CHOICES=[
        ('none', 'none'),
        ('advancedDiscussion', 'advancedDiscussion'),
        ('readyToJoin', 'readyToJoin'),
        ('visiting', 'visiting'),
        ('feesNegotiation', 'feesNegotiation'),
        ('batchAllocation', 'batchAllocation'),
        ('interestedDemo', 'interestedDemo'),
        ('needTimeThisWeek', 'needTimeThisWeek'),
        ('needTimeNextWeek', 'needTimeNextWeek'),
        ('needTimeThisMonth', 'needTimeThisMonth'),
        ('needTimeNextMonth', 'needTimeNextMonth'),
        ('specialRequirements', 'specialRequirements'),
        ('paymentLinkSent', 'paymentLinkSent'),
        ('closedOwnRegister', 'closedOwnRegister'),
        ('busyAskedACallBack', 'busyAskedACallBack'),
        ('closedLost', 'closedLost')

        ]
        
    Attended_Demo= models.CharField(
        max_length=30,
        choices= ATTEND_DEMO_CHOICES,
        default='None',
    )
    Learner_Stage =  models.CharField(
        max_length=30,
        choices=LEARNER_STAGE_CHOICES,
        default='None',
    )
    Location= models.CharField(
        max_length=30,
        choices=LOCATION_CHOICES,
        default='None',
    )
    

