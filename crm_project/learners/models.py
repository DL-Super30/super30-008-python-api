from django.db import models
from django.utils import timezone

class learners(models.Model):
    First_Name = models.CharField(max_length=225)
    Last_Name =  models.CharField(max_length=225)
    Id_Proof = models.CharField(max_length=100)
    Phone = models.BigIntegerField()
    Date_OF_Birth = models.DateField(default=timezone.now)
    Email = models.EmailField(max_length=225)
    Registered_Date =  models.DateField(default=timezone.now)
    Batch_Id =  models.CharField(max_length=100)
    Alternate_Phone = models.BigIntegerField()
    Description =  models.TextField()
    Source = models.CharField()
    Learner_Owner = models.IntegerField()
    Currency = models.DecimalField(max_digits=10, decimal_places=3)
    Exchange_Rate = models.DecimalField(max_digits=10, decimal_places=3)
    Lead_Created_Time =  models.DateField(default=timezone.now)
    Registered_Course = models.IntegerField()
    Tech_Stack = models.CharField(max_length=100)
    Course_Comments = models.CharField(max_length=100)
    Slack_Access = models.CharField(max_length=100)
    LMS_Access = models.CharField(max_length=100)
    Mode_Of_Class = models.CharField(max_length=100)
    Comment = models.CharField(max_length=100)
    Preferable_Time=  models.DateField(default=timezone.now)
    Batch_Timing = models.DateField(default=timezone.now)

    ATTEND_DEMO_CHOICES=[
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
    LEARNER_STAGE_CHOICES=[
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
        ('Closed Own Register', 'Closed Own Register')


    ]
    LOCATION_CHOICES=[
        ('None', 'None'),
        ('Advanced Discussion', 'Advanced Discussion'),
        ('Ready To Join', 'Ready To Join'),
        ('Visiting', 'Visiting'),
        ('Fees Negotiation', 'Fees Negotiation'),
        ('Batch Allocation', 'Batch Allocation'),
        ('Interested Demo', 'Interested Demo'),
        ('Need Time This Week', 'Need Time This Week'),
        ('Need Time Next Week', 'Need Time Next Week'),
        ('Need Time This Month', 'Need Time This Month'),
        ('Need Time Next Month', 'Need Time Next Month'),
        ('Special Requirements', 'Special Requirements'),
        ('Payment Link Sent', 'Payment Link Sent'),
        ('Closed Own Register', 'Closed Own Register'),
        ('Busy Asked A Call Back', 'Busy Asked A Call Back'),
        ('Closed Lost', 'Closed Lost')


    ]
    COUNSELING_CHOICES = [
        ('True', 'True'),
        ('False', 'False')
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
    Counseling_Done_By = models.CharField(
        max_length=5,
        choices=COUNSELING_CHOICES,
        default='False'
    )
    

