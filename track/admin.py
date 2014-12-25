from django.contrib import admin
from track.models import HoldingType, Holding, AllocationRule

admin.site.register(HoldingType)
admin.site.register(Holding)
admin.site.register(AllocationRule)
