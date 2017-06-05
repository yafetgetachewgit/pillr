from django.contrib import admin
from .models import Doctor, Institute, Pharmacy
from dashboard.models import Drug


# Register your models here.

admin.site.register(Doctor)
admin.site.register(Institute)
admin.site.register(Pharmacy)
admin.site.register(Drug)

