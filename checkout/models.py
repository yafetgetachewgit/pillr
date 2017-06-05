from django.db import models
from dashboard.models import Prescription

class PrescriptionStatus(models.Model):
    prescription = models.ForeignKey(Prescription)
    checkedOut = models.BooleanField(default=False)

    def __unicode__(self):
        return "Checked Out" + self.checkedOut
