# Generated by Django 4.2.2 on 2023-06-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_role', models.CharField(max_length=100)),
                ('accepting_applicsations', models.BooleanField(default=True)),
                ('received_applications', models.IntegerField(blank=True, null=True)),
                ('number_people_to_hire', models.IntegerField()),
            ],
        ),
    ]
