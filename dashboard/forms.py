from django import forms
from .models import Prescription, Drug
from datetimewidget.widgets import DateTimeWidget
from users.models import Patient


class PrescriptionForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    time_between_treatments = forms.FloatField(widget=forms.TextInput, label='Time Between Treatments')
    drug = forms.ModelChoiceField(queryset=Drug.objects.all())


    class Meta:

	    model = Prescription
	    fields = ['drug', 'prognosis', 'patient', 'total_doses', 'start_date', 'doses', 'time_between_treatments', 'the_time_is_in', 'treatment_duration_days']
