from django.db import models
from django.contrib.auth.models import User


# User information, applies to all users
class UserInfo(models.Model):

    user = models.OneToOneField(User)


    class Meta:
        abstract = True

# Patient information, applies to patients


class Doctor(UserInfo):

    specialty = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    licenced = models.BooleanField(default=1)

    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name + " M.D."


class Patient(UserInfo):

    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    doctors = models.ManyToManyField(Doctor, null=False)
    active = models.BooleanField(default=True)
    region = models.CharField(max_length=100, default="n/a")

    def __unicode__(self):
        return self.user.username

class Institute(UserInfo):
    institution = models.CharField(max_length=100, default="Uknown institution")

class Pharmacy(UserInfo):
    farmacy = models.CharField(max_length=100)
