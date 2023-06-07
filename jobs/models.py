from django.db import models


# Create your models here.
class Job(models.Model):
    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    accepting_applicsations = models.BooleanField(default=True,)
    received_applications = models.IntegerField(blank=True, null=True)
    number_people_to_hire = models.IntegerField()

    