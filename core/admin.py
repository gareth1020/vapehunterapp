from django.contrib import admin
import core.models as coremodels
# Register your models here.

admin.site.register(coremodels.Manufacturer)
admin.site.register(coremodels.Eliquid)
admin.site.register(coremodels.Review)
admin.site.register(coremodels.Profile)