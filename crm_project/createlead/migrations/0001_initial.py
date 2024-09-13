# Generated by Django 5.1.1 on 2024-09-12 10:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateLeads',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('cc', models.BigIntegerField()),
                ('contact_no', models.BigIntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('fee_coated', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('batch_timing', models.CharField(choices=[('7AM_8AM', '7AM_8AM'), ('8AM_9AM', '8AM_9AM'), ('9AM_10AM', '9AM_10AM'), ('10AM_11AM', '10AM_11AM'), ('11AM_12PM', '11AM_12PM'), ('12PM_1PM', '12PM_1PM'), ('1PM_2PM', '1PM_2PM'), ('2PM_3PM', '2PM_3PM'), ('3PM_4PM', '3PM_4PM'), ('4PM_5PM', '4PM_5PM'), ('5PM_6PM', '5PM_6PM'), ('6PM_7PM', '6PM_7PM'), ('7PM_8PM', '7PM_8PM'), ('8PM_9PM', '8PM_9PM')], default='7AM_8AM', max_length=10)),
                ('lead_status', models.CharField(choices=[('Not Contacted', 'Not Contacted'), ('Attempted', 'Attempted'), ('Warm Lead', 'Warm Lead'), ('Cold Lead', 'Cold Lead')], default='None', max_length=13)),
                ('lead_source', models.CharField(choices=[('None', 'None'), ('WalkIn', 'WalkIn'), ('StudentReferral', 'StudentReferral'), ('Demo', 'Demo'), ('WebSite', 'WebSite'), ('WebsiteChat', 'WebsiteChat'), ('InboundCall', 'InboundCall'), ('GoogleAdWords', 'GoogleAdWords'), ('FacebookAds', 'FacebookAds'), ('GoogleMyBusiness', 'GoogleMyBusiness'), ('WhatsAppSkillCapital', 'WhatsAppSkillCapital')], default='None', max_length=24)),
                ('TechStack', models.CharField(choices=[('Life Skills', 'Life Skills'), ('Study Abroad', 'Study Abroad'), ('HR', 'HR')], default='Select Stack', max_length=24)),
                ('Course', models.CharField(choices=[('HR Business Partner', 'HR Business Partner'), ('HR Generalist Core HR', 'HR Generalist Core HR'), ('HR Analytics', 'HR Analytics'), ('Spoken English', 'Spoken English'), ('Public Speaking', 'Public Speaking'), ('Communication Skills', 'Communication Skills'), ('Soft Skills', 'Soft Skills'), ('Personality Development', 'Personality Development'), ('Aptitude', 'Aptitude'), ('IELTS', 'IELTS'), ('TOEFL', 'TOEFL'), ('PTE', 'PTE'), ('GRE', 'GRE'), ('GMAT', 'GMAT'), ('Recruitment Specialist', 'Recruitment Specialist'), ('Payroll Specialist', 'Payroll Specialist'), ('Learning and Development', 'Learning and Development'), ('Others', 'Others'), ('Finance', 'Finance'), ('Competitive Exams', 'Competitive Exams'), ('HR Manage', 'HR Manage')], default='None', max_length=24)),
                ('class_mode', models.CharField(choices=[('International Online', 'International Online'), ('India Online', 'India Online'), ('BLR Classroom', 'BLR Classroom'), ('HYD Classroom', 'Hyd Classroom')], default='HYDClassRoom', max_length=24)),
            ],
        ),
    ]
