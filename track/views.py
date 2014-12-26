from django.shortcuts import render
from track.models import AllocationRule, HoldingType, Holding
from decimal import *

def index(request):
    new_amount = 0
    total = 0
    if 'new_amount' in request.POST:
        new_amount = Decimal(request.POST['new_amount'])
        total = new_amount

    max_amounts = {}
    for ht in Accounts.objects.all():
        max_amounts.setdefault(ht.name, 0)

    current_investments = {}
    for ht in HoldingType.objects.all():
        for h in Holding.objects.filter(holding__name=ht.name):
            current_investments[ht.name] = current_investments.setdefault(ht.name, 0) + h.amount
            max_amounts[h.account] += h.amount
            total += h.amount

    ideal_investments = []
    for ar in AllocationRule.objects.all().order_by('holding_id'):
        amt = ar.percent * total / 100
        ideal_investments.append([ar.holding_type.name, current_investments[ar.holding_type.name], amt])
    context = {'new_amount' : new_amount,
               'total' : total,
               'ideal' : ideal_investments,
               'max_amounts' : max_amounts}
    return render(request, 'track/index.html', context)

