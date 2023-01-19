# Generated by Django 4.1.2 on 2022-10-31 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacation_management_app', '0003_alter_account_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='status',
            field=models.CharField(choices=[('VI', 'Viewer'), ('EM', 'Employee')], max_length=2, null=True),
        ),
    ]