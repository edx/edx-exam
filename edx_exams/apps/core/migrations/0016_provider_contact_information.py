# Generated by Django 3.2.18 on 2023-04-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_exam_only one exam instance active'),
    ]

    operations = [
        migrations.AddField(
            model_name='proctoringprovider',
            name='tech_support_email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='proctoringprovider',
            name='tech_support_phone',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
