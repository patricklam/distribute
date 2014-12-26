from django.shortcuts import render
from track.models import HoldingTypeProportionRule, HoldingType, Holding, Account
from decimal import *

def index(request):
    new_amount = 0
    total = 0
    if 'new_amount' in request.POST:
        new_amount = Decimal(request.POST['new_amount'])
        total = new_amount

    amounts = {}
    for ht in Account.objects.all():
        amounts.setdefault(ht, 0)

    current_investments = {}
    for ht in HoldingType.objects.all():
        for h in Holding.objects.filter(holding_type__name=ht.name):
            current_investments[ht.name] = current_investments.setdefault(ht.name, 0) + h.amount
            amounts[h.account] += h.amount
            total += h.amount

    max_amounts = {}
    for ht in Account.objects.all():
        if ht.can_add_money:
            m = "N/A"
        else:
            m = amounts[ht]
        max_amounts[ht] = (amounts[ht], m)

    ideal_investments = []

    for ar in HoldingTypeProportionRule.objects.all().order_by('holding_type__name'):
        amt = ar.percent * total / 100
        ideal_investments.append([ar.holding_type.name, current_investments.setdefault(ar.holding_type.name, 0), amt])

    context = {'new_amount' : new_amount,
               'total' : total,
               'ideal' : ideal_investments,
               'max_amounts' : max_amounts}
    return render(request, 'track/index.html', context)

