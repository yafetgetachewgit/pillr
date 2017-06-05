from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from timeline.models import Feedback, ScheduleScore
from dashboard.models import Drug

@login_required
def index(request):

    data = {}
    feedbacks = Feedback.objects.all();


    for f in feedbacks:
        drug = str(f.prescription.drug.drug_name)

        if not data.get(drug) is None:
            increase(data, drug, f.rating)
        else:
            reset(data, drug)
            increase(data, drug, f.rating)

    scores = ScheduleScore.objects.all()[5:]

    return render(request, 'dss/index.html', {"data_feedback":data, "scores": scores})


def increase(data, drug, rating):

    if rating == 0:
        data[drug]['worse'] += 1
    elif rating == 1:
        data[drug]['same'] += 1
    else:
        data[drug]['better'] += 1

def reset(data, drug):
    data[drug] = {}
    data[drug]['better'] = 0
    data[drug]['same'] = 0
    data[drug]['worse'] = 0