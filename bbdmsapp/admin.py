from django.contrib import admin
from bbdmsapp.models import DonorReg, BloodRequest ,Bloodgroup,Contact
# Register your models here.
admin.site.register(DonorReg)
admin.site.register(BloodRequest)
admin.site.register(Bloodgroup)
admin.site.register(Contact)
