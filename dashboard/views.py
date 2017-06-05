from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PrescriptionForm
from users.models import Doctor, Patient
from django.contrib.auth.models import User, Group


@login_required
def index(request):
	user = User.objects.get(pk=request.user.id)
	if not user.groups.filter(name="doctors"):
		return render(request, 'dashboard/unauthorized.html')
	else:

		patients = 3
		return render(request, 'dashboard/index.html')


@login_required
def prescribe(request):

	user = User.objects.get(pk=request.user.id)
	if not user.groups.filter(name="doctors"):
		return render(request, 'dashboard/unauthorized.html')

	if request.method == 'POST':
		prescription_form = PrescriptionForm(data=request.POST)

		if prescription_form.is_valid():
			prescription = prescription_form.save(commit=False)
			thisdoc = Doctor.objects.get(user_id=request.user.id)
			prescription.doctor_id = thisdoc.id
			prescription.total_score = prescription.total_doses * 2
			prescription.doses_remaining = prescription.total_doses
			prescription.save()
			return render(request, 'dashboard/index.html')

		else:
			prescription_form = PrescriptionForm(data=request.POST)
		return render(request, 'dashboard/prescribe.html', {'prescription_form': prescription_form})

	else:
		thisuser = User.objects.get(id=request.user.id)
		thisuser
		prescription_form = PrescriptionForm()
		return render(request, 'dashboard/prescribe.html', {'prescription_form': prescription_form})

@login_required
def pharma(request):

	user = User.objects.get(pk=request.user.id)
	if not user.groups.filter(name="pharma"):
		return render(request, 'dashboard/unauthorized.html')

	return render(request, 'dashboard/pharma.html')

