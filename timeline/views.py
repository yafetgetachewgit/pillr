from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from forms import FeedbackForm
from dashboard.models import Prescription
from users.models import Patient
from .models import Feedback, ScheduleScore


@login_required
def index(request):
    user_id = request.user.id
    patient = Patient.objects.filter(user_id = user_id)
    patient_id = patient.first().id
    user_prescriptions = Prescription.objects.filter(patient_id = patient_id)
    doctors = []
    total_score = 0
    for i in user_prescriptions:
        total_score += i.total_score
        if doctors == []:
            doctors.append(i.doctor)
        else:
            for d in doctors:
                if not i.doctor == d:
                    doctors.append(i.doctor)
                    print(i.doctor)



    feedbacks = Feedback.objects.filter(patient_id = patient_id)

    scores = ScheduleScore.objects.filter(patient_id = patient_id)

    score = 0
    for s in scores:
        score += s.score

    return render(request, 'timeline/index.html', {"prescriptions":user_prescriptions, "doctors":doctors, "feedbacks": feedbacks, "score":score, "total_score":total_score})


def timeline_detail(request, detail_level):
	return HttpResponse("You timeline overview by %s" % detail_level)


def feedback(request):
	feedback_form = FeedbackForm()
	return render(request, "timeline/feedback.html", {"feedback_form": feedback_form})
