# Generated by Django 5.1 on 2024-09-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="leads",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=100)),
                ("Phone", models.BigIntegerField()),
                ("CC", models.BigIntegerField(default=91)),
                ("Email", models.EmailField(default="N/A", max_length=254)),
                (
                    "Fee_Quoted",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
                ),
                ("Description", models.TextField(default="N/A", max_length=300)),
                (
                    "Lead_Source",
                    models.CharField(
                        choices=[
                            ("None", "None"),
                            ("WalkIn", "WalkIn"),
                            ("StudentReferral", "StudentReferral"),
                            ("Demo", "Demo"),
                            ("WebSite", "WebSite"),
                            ("WebsiteChat", "WebsiteChat"),
                            ("InboundCall", "InboundCall"),
                            ("GoogleAdWords", "GoogleAdWords"),
                            ("FacebookAds", "FacebookAds"),
                            ("GoogleMyBusiness", "GoogleMyBusiness"),
                            ("WhatsAppDigitalLync", "WhatsAppDigitalLync"),
                        ],
                        default="None",
                        max_length=20,
                    ),
                ),
                (
                    "Class_Mode",
                    models.CharField(
                        choices=[
                            ("HYDClassRoom", "HYDClassRoom"),
                            ("BLRClassRoom", "BLRClassRoom"),
                            ("IndiaOnline", "IndiaOnline"),
                            ("InternationalOnline", "InternationalOnline"),
                        ],
                        default="HYDclassrrom",
                        max_length=20,
                    ),
                ),
                (
                    "Lead_Status",
                    models.CharField(
                        choices=[
                            ("None", "None"),
                            ("Not contacted", "Not contacted"),
                            ("Attempted", "Attempted"),
                            ("warm lead", "warm lead"),
                            ("opportunity", "opportunity"),
                            ("attendedemo", "attendedemo"),
                            ("visited", "visited"),
                            ("registered", "registered"),
                            ("coldlead", "coldlead"),
                        ],
                        default="None",
                        max_length=20,
                    ),
                ),
                (
                    "Course",
                    models.CharField(
                        choices=[
                            ("Angulaar", "Angulaar"),
                            ("AWS", "AWS"),
                            ("AWSWithDevOps", "AWSWithDevOps"),
                            ("Azure", "Azure"),
                            ("AzureDevOps", "AzureDevOps"),
                            ("BusinessAnlayst", "BusinessAnlayst"),
                            ("CloudOpsMasters", "CloudOpsMasters"),
                            ("DevOps", "DevOps"),
                            ("FrontEndAngular", "FrontEndAngular"),
                            ("FrontEndReact", "FrontEndReact"),
                            ("FullStackJAVA", "FullStackJAVA"),
                            ("FullStackMEAN", "FullStackMEAN"),
                            ("FullStackMERN", "FullStackMERN"),
                            ("FullstackPython", "FullstackPython"),
                            ("FullStackReactJAVA", "FullStackReactJAVA"),
                            ("Java", "Java"),
                            ("NeedCounselling", "NeedCounselling"),
                            ("Others", "Others"),
                            ("PowerBI", "PowerBI"),
                            ("Python", "Python"),
                            ("React", "React"),
                            ("SalesForceAdmin", "SalesForceAdmin"),
                            ("SalesforceDeveloper", "SalesforceDeveloper"),
                            ("ServiceNow", "ServiceNow"),
                            ("AzureDataEngineer", "AzureDataEngineer"),
                            ("Tableau", "Tableau"),
                            ("Testing", "Testing"),
                        ],
                        default="None",
                        max_length=20,
                    ),
                ),
                (
                    "Stack",
                    models.CharField(
                        choices=[
                            ("CloudOps", "CloudOps"),
                            ("Salesforce", "Salesforce"),
                            ("FullStack", "FullStack"),
                            ("DataStack", "DataStack"),
                            ("ServiceNow", "ServiceNow"),
                            ("BusinessStack", "BusinessStack"),
                            ("CareerCounselling", "CareerCounselling"),
                        ],
                        default="None",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
