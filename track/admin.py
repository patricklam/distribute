from django.contrib import admin
from track.models import HoldingType, Holding, AllocationRule, Account, LocationRule

admin.site.register(HoldingType)
admin.site.register(Account)
admin.site.register(Holding)
admin.site.register(AllocationRule)
admin.site.register(LocationRule)
