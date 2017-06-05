from django.db import models
from users.models import Patient
from dashboard.models import Prescription
# Create your models here.


class Feedback(models.Model):

    BETTER = 2
    SAME = 1
    WORSE = 0

    PROGRESS = ((BETTER, 'I am feeling better'),
                       (SAME, 'No change in my health'),
                       (WORSE, 'I am getting worse'),
                       )

    patient = models.ForeignKey(Patient, default=None)
    prescription = models.ForeignKey(Prescription, unique=False)
    rating = models.IntegerField(choices=PROGRESS, default=BETTER)
    comment = models.CharField(max_length=300)
    post_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.patient.id + " " + self.prescription.drug_name

class Schedule (models.Model):
    patient = models.ForeignKey(Patient)
    prescription = models.OneToOneField(Prescription)
    priority = models.IntegerField()

class Questionnaire(models.Model):
    question = models.CharField(max_length=100)
    choices = models.CharField(max_length=100)
    answers = models.CharField(max_length=100, default=None)

class ScheduleScore(models.Model):

    MISSED = 0
    DELAYED = 1
    TAKEN = 2

    SCORE = ((MISSED, "You missed taking this prescription"),
             (DELAYED, "You were late in taking this prescription"),
             (TAKEN, "You have taken this drug on time"))

    prescription = models.ForeignKey(Prescription, unique=False)
    score = models.IntegerField(choices=SCORE, default=TAKEN)
    prescription_missed = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient)
