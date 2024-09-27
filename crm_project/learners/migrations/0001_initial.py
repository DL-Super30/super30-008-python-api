# Generated by Django 5.1.1 on 2024-09-27 09:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='learners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=225)),
                ('LastName', models.CharField(max_length=225)),
                ('IdProof', models.CharField(max_length=100)),
                ('Phone', models.BigIntegerField()),
                ('DateofBirth', models.DateField(default=django.utils.timezone.now)),
                ('Email', models.EmailField(max_length=225)),
                ('RegisteredDate', models.DateField(default=django.utils.timezone.now)),
                ('BatchId', models.CharField(max_length=100)),
                ('Alternatephone', models.BigIntegerField()),
                ('Description', models.TextField()),
                ('Source', models.CharField()),
                ('LearnerOwner', models.IntegerField()),
                ('Currency', models.DecimalField(decimal_places=3, max_digits=10)),
                ('CounselingDoneBY', models.BooleanField(default=False)),
                ('ExchangeRate', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Leadcratedtime', models.DateField(default=django.utils.timezone.now)),
                ('RegisteredCourse', models.IntegerField()),
                ('TechStack', models.CharField(max_length=100)),
                ('CourseComments', models.CharField(max_length=100)),
                ('SlackAccess', models.CharField(max_length=100)),
                ('LMSAccess', models.CharField(max_length=100)),
                ('ModeOfClass', models.CharField(max_length=100)),
                ('Comment', models.CharField(max_length=100)),
                ('PreferableTime', models.DateField(default=django.utils.timezone.now)),
                ('BatchTiming', models.DateField(default=django.utils.timezone.now)),
                ('Attended_Demo', models.CharField(choices=[('None', 'None'), ('Ready To Join', 'Ready To Join'), ('Advanced Discussion', 'Advanced Discussion'), ('Call Not Answered', 'Call Not Answered'), ('Visiting', 'Visiting'), ('Fees Negotiation', 'Fees Negotiation'), ('Batch Allocation', 'Batch Allocation'), ('Need Time This Week', 'Need Time This Week'), ('Need Time Next Week', 'Need Time Next Week'), ('Need Time This Month', 'Need Time This Month'), ('Need Time Next Month', 'Need Time Next Month'), ('special Requirements', 'special Requirements'), ('Closed Own (Register) ', 'Closed Own (Register) '), ('Closed Lost (Cold Lead) ', 'Closed Lost (Cold Lead) ')], default='None', max_length=30)),
                ('Learner_Stage', models.CharField(choices=[('None', 'None'), ('Call Not Answered', 'Call Not Answered'), ('Ready To Join', 'Ready To Join'), ('Fees Negotiation', 'Fees Negotiation'), ('Batch Allocation', 'Batch Allocation'), ('Intrested Demo', 'Intrested Demo'), ('Special Requirements ', 'Special Requirements '), ('Need Time This Week', 'Need Time This Week'), ('Need Time Next Week', 'Need Time Next Week'), ('Need Time This Month', 'Need Time This Month'), ('Need Time Next Month', 'Need Time Next Month'), ('Closed Own (Register) ', 'Closed Own (Register) ')], default='None', max_length=30)),
                ('Location', models.CharField(choices=[('None', 'None'), ('Advanced Discussion', 'Advanced Discussion'), ('Ready To Join', 'Ready To Join'), ('Visiting', 'Visiting'), ('Fees Negotiation', 'Fees Negotiation'), ('Batch Allocation', 'Batch Allocation'), ('Intrested Demo', 'Intrested Demo'), ('Need Time This Week', 'Need Time This Week'), ('Need Time Next Week', 'Need Time Next Week'), ('Need Time This Month', 'Need Time This Month'), ('Need Time Next Month', 'Need Time Next Month'), ('Special Requirements ', 'Special Requirements '), ('payment Link Sent', 'payment Link Sent'), ('Closed Own (Register) ', 'Closed Own (Register) '), ('Busy & Asked a Call Back ', 'Busy & Asked a Call Back'), ('Closed Lost', 'Closed Lost')], default='None', max_length=30)),
            ],
        ),
    ]
