from django.db import models
from users.models import Patient, Doctor


class Drug(models.Model):
    drug_name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.drug_name

class Prescription(models.Model):
    HOUR = 'HR'
    DAY = 'DD'
    WEEK = 'WK'
    MONTH = 'MM'
    YEAR = 'YY'

    SUCCESS = 1
    FAILURE = 0

    EVERY_X_CHOICES = ((HOUR, 'Hour(s)'),
                       (DAY, 'Day(s)'),
                       (WEEK, 'Week(s)'),
                       (MONTH, 'Month(s)'),
                       (YEAR, 'Year(s)'),
                       )
    OUTCOME = (
                (SUCCESS, 'Successful'),
               (FAILURE, 'Failed'),
               )

    date = models.DateTimeField(auto_now_add=True)
    prognosis = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, unique=False)
    doctor = models.ForeignKey(Doctor, unique=False)
    total_doses = models.IntegerField()
    start_date = models.DateTimeField()
    drug = models.ForeignKey(Drug, unique=False, null=True)
    treatment_duration_days = models.IntegerField(default=3)
    doses = models.IntegerField(default=1)
    time_between_treatments = models.FloatField(default=1)
    the_time_is_in = models.CharField(max_length=2, choices=EVERY_X_CHOICES, default=DAY)
    confirmed = models.BooleanField(default=False)
    total_score = models.IntegerField(default=0, null=False)
    doses_remaining = models.IntegerField(default=0, null=False)
    outcome = models.IntegerField(choices=OUTCOME, default=FAILURE)

    def __unicode__(self):
        return self.prognosis



