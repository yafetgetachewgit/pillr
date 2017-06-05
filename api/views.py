from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from dashboard.permissions import IsOwnerOrReadOnly
from dashboard.models import Prescription
from dashboard.serializers import PrescriptionSerializer
from users.models import Patient
from timeline.models import Feedback, ScheduleScore


def test(request):
	return HttpResponse("Hi")


def testjson(request):
	response={}
	response["method"] = request.method
	response["message"] = "Message From Server via json"

	return JsonResponse(response)



class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


class WhoAmI(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

	def get(self, request, format=None):


		response = {}
		response["auth"] = request.user.is_authenticated()
		response["email"] = request.user.email
		response["is_staff"] = request.user.is_staff
		response["is_active"] = request.user.is_active
		response["last_login"] = request.user.last_login

		# response["prescription"] = JSONResponse(serializer.data)


		return JsonResponse(response)

class DataRequest(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

	def get(self, request, format=None):

		requesting_user = User.objects.filter(username = self.request.user)
		requesting_user_pid = Patient.objects.filter(user_id = requesting_user.first().id)
		prescriptions = Prescription.objects.filter(patient_id = requesting_user_pid)

		serializer = PrescriptionSerializer(prescriptions.order_by("date").reverse(), many=True)

		print "REQUESTED SOME DATA"
		print self.request.user
		response = {}
		response["data"] = JSONResponse(serializer.data)



		#response["data"] = serializer.data
		#print(serializer.data)
		return JsonResponse(serializer.data, safe=False)


class DataSubmit(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
	parser_classes = (JSONParser, )

	def post(self, request, format=None):
		postData =  request.data
		response = {}
		requesting_user = User.objects.filter(username = self.request.user)
		requesting_user_pid = Patient.objects.filter(user_id = requesting_user.first().id)

		if postData.get("type") == "feedback":

			feedback = Feedback(rating = postData.get("rating"), comment = postData.get("comment"), prescription_id = postData.get("id"),
								patient_id = requesting_user_pid.first().id)
			print postData.get("rating")
			feedback.save()
			response["outcome"] = "success"

		elif postData.get("type") == "score":


			score = ScheduleScore(score = postData.get("score"), prescription_id = postData.get("prescription_id"), patient_id = requesting_user_pid.first().id)
			score.save()

			print postData.get("score")

			if postData.get("score") == "2":
				prescription = Prescription.objects.get(pk = postData.get("prescription_id"))
				print prescription.doses_remaining
				if prescription.doses_remaining > 0:
					print "hi"
					prescription.doses_remaining -= 1
					prescription.save()

			response["outcome"] = "success"

		else:
			response["outcome"] = "failed"

		return JsonResponse(response)


