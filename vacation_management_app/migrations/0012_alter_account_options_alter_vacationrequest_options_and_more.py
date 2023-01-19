# Generated by Django 4.1.2 on 2022-11-03 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacation_management_app', '0011_alter_vacationrequest_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'User Status', 'verbose_name_plural': 'User Statuses'},
        ),
        migrations.AlterModelOptions(
            name='vacationrequest',
            options={'verbose_name': 'Vacation Request'},
        ),
        migrations.AddField(
            model_name='vacationrequest',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacation_management_app.account'),
        ),
    ]
