from django.contrib import admin
from track.models import HoldingType, Holding, HoldingTypeProportionRule, Account, HoldingLocationRule

admin.site.register(HoldingType)
admin.site.register(Account)
admin.site.register(Holding)
admin.site.register(HoldingTypeProportionRule)
admin.site.register(HoldingLocationRule)
