# Generated by Django 4.2.1 on 2023-05-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_requests_issue_time_alter_requests_return_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='request_time',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
