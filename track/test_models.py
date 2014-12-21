from django.test import TestCase
from track.models import HoldingType, AllocationRule

class SampleData(TestCase):
    def setUp(self):    
        tdb900 = HoldingType(name="TDB900",asset_class="equity",country="CA")
        tdb902 = HoldingType(name="TDB902",asset_class="equity",country="US")
        tdb909 = HoldingType(name="TDB909",asset_class="bond",country="CA")
        tdb911 = HoldingType(name="TDB911",asset_class="equity",country="INTL")

        cdn_bonds = AllocationRule(percent=40, holding=tdb909)
        cdn_stock = AllocationRule(percent=20, holding=tdb900)
        us_stock  = AllocationRule(percent=20, holding=tdb902)
        intl_stock= AllocationRule(percent=20, holding=tdb911)
