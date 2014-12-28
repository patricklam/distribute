from django.shortcuts import render
from track.models import HoldingTypeProportionRule, HoldingType, Holding, Account, HoldingLocationRule
from decimal import *
from datetime import date

def calculate_raw_allocations(total, current_investments):
    raw_allocations = [] #: according to the rules, how much of each holding (1) currently held; (2) to hold
    remaining_amount_to_allocate = {} #: amount still to allocate, for each holding type
    for ar in HoldingTypeProportionRule.objects.all().order_by('holding_type__name'):
        amt = ar.percent * total / 100
        raw_allocations.append([ar.holding_type.name, current_investments.setdefault(ar.holding_type.name, 0), amt])
        remaining_amount_to_allocate[ar.holding_type] = remaining_amount_to_allocate.setdefault(ar.holding_type, 0) + amt
    return (raw_allocations, remaining_amount_to_allocate)

def index(request):
    new_amount = 0 #: amount of money to add
    total = 0 #: total pool of money available
    if 'new_amount' in request.POST:
        new_amount = Decimal(request.POST['new_amount'])
        total = new_amount

    amounts = {} #: amount of money already in each account
    for ht in Account.objects.all():
        amounts.setdefault(ht, 0)

    current_investments = {} #: amount of money per holding type
    for ht in HoldingType.objects.all():
        for h in Holding.objects.filter(holding_type__name=ht.name):
            current_investments[ht.name] = current_investments.setdefault(ht.name, 0) + h.amount
            amounts[h.account] += h.amount
            total += h.amount

    max_amounts = {} #: max amount of money one can put in an account, or N/A
    room_left = {} #: running total of room left in each account
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

    # calculate the dollar amounts for each holding type
    raw_allocations, remaining_amount_to_allocate = calculate_raw_allocations(total, current_investments)

    allocated_amounts = {}
    for lr in HoldingLocationRule.objects.all().order_by('priority'):
        for a in Account.objects.filter(account_type = lr.account_type):
            remaining_amount = remaining_amount_to_allocate[lr.holding_type]
            allocated_amounts.setdefault(a, [])
            h = Holding()
            h.account = a
            h.holding_type = lr.holding_type
            h.purchase_date = date.today()
            if (room_left[a] == 'N/A' or room_left[a] > remaining_amount):
                h.amount = remaining_amount
                allocated_amounts[a].append((h, remaining_amount))
                remaining_amount_to_allocate[lr.holding_type] = 0
                if room_left[a] != 'N/A':
                    room_left[a] -= remaining_amount
            else:
                h.amount = room_left[a]
                allocated_amounts[a].append((h, room_left[a]))
                remaining_amount_to_allocate[lr.holding_type] -= room_left[a]
                if room_left[a] != 'N/A':
                    room_left[a] = 0

    for a in allocated_amounts:
        for h in allocated_amounts[a]:
            found = False
            for idx, ch in enumerate(current_holdings_per_account[a]):
                if ch[0].holding_type == h[0].holding_type:
                    found = True
                    current_holdings_per_account[a][idx] = (ch[0], ch[1] + h[1])
            if not found and h[1] > 0:
                current_holdings_per_account[a].append((h[0], h[1]))

    context = {'new_amount' : new_amount,
               'total' : total,
               'raw' : raw_allocations,
               'max_amounts' : max_amounts,
               'current_holdings_pa' : current_holdings_per_account}
    return render(request, 'track/index.html', context)

