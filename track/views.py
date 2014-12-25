from django.shortcuts import render
from track.models import AllocationRule, HoldingType, Holding
from decimal import *

def index(request):
    amount = 0
    if 'amount' in request.POST:
        amount = Decimal(request.POST['amount'])

    current_investments = []
    for ht in HoldingType.objects.all().order_by('name'):
        ciSum = 0
        for h in Holding.objects.filter(holding__name=ht.name):
            ciSum += h.amount
        current_investments.append([ht.name, ciSum])

    ideal_investments = []
    for ar in AllocationRule.objects.all().order_by('holding_id'):
        amt = ar.percent * amount / 100
        ideal_investments.append([ar.holding.name, amt])
    context = {'amount' : amount,
               'table_contents' : current_investments}
    return render(request, 'track/index.html', context)

