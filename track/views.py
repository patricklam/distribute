from django.shortcuts import render
from track.models import HoldingTypeProportionRule, HoldingType, Holding, Account, HoldingLocationRule
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
    room_left = {}
    current_holdings_per_account = {}
    for a in Account.objects.all():
        if a.can_add_money:
            m = "N/A"
        else:
            m = amounts[a]
        max_amounts[a] = (amounts[a], m)
        room_left[a] = m
        for ht in Holding.objects.filter(account=a):
            if not (a in current_holdings_per_account):
                current_holdings_per_account[a] = []
            current_holdings_per_account[a].append((ht, 0))

    ideal_investments = []
    remaining_amount_to_allocate = {}
    for ar in HoldingTypeProportionRule.objects.all().order_by('holding_type__name'):
        amt = ar.percent * total / 100
        ideal_investments.append([ar.holding_type.name, current_investments.setdefault(ar.holding_type.name, 0), amt])
        remaining_amount_to_allocate[ar.holding_type] = remaining_amount_to_allocate.setdefault(ar.holding_type, 0) + amt

    allocated_amounts = {}
    for lr in HoldingLocationRule.objects.all().order_by('priority'):
        for a in Account.objects.filter(account_type = lr.account_type):
            remaining_amount = remaining_amount_to_allocate[lr.holding_type]
            allocated_amounts.setdefault(a, [])
            if (room_left[a] == 'N/A' or room_left[a] > remaining_amount):
                allocated_amounts[a].append((lr.holding_type, remaining_amount))
                remaining_amount_to_allocate[lr.holding_type] = 0
                if room_left[a] != 'N/A':
                    room_left[a] -= remaining_amount
            else:
                allocated_amounts[a].append((lr.holding_type, room_left[a]))
                remaining_amount_to_allocate[lr.holding_type] -= room_left[a]
                if room_left[a] != 'N/A':
                    room_left[a] = 0

    # todo merge allocated_amounts with current_holdings_per_account

    context = {'new_amount' : new_amount,
               'total' : total,
               'ideal' : ideal_investments,
               'max_amounts' : max_amounts,
               'current_holdings_pa' : current_holdings_per_account,
               'allocated_amounts' : allocated_amounts}
    return render(request, 'track/index.html', context)

