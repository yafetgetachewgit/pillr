from django.conf.urls import url, include
from rest_framework import routers
from . import views
from rest_framework.authtoken import views as rest_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^test/$', views.test, name='test'),
	url(r'^json/$', views.testjson, name='testjson'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^token-me/', rest_views.obtain_auth_token),
	url(r'^whoami/', views.WhoAmI.as_view(), name='secret-view'),
    url(r'^request_data/', views.DataRequest.as_view(), name='data-view'),
    url(r'^submit_data/', views.DataSubmit.as_view(), name='submit-view'),
]

