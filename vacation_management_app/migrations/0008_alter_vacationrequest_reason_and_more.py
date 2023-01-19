# Generated by Django 4.1.2 on 2022-10-31 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacation_management_app', '0007_vacationrequest_alter_account_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacationrequest',
            name='reason',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='vacationrequest',
            name='status',
            field=models.CharField(choices=[('WG', 'Waiting'), ('AD', 'Approved'), ('RD', 'Rejected')], default='WG', max_length=2),
        ),
    ]
