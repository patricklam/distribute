from django.shortcuts import render
from track.models import AllocationRule
from decimal import *

def index(request):
    amount = 0
    if 'amount' in request.POST:
        amount = Decimal(request.POST['amount'])
    investments = []
    for ar in AllocationRule.objects.all():
        amt = ar.percent * amount / 100
        investments.append([ar.holding.name, amt])
    context = {'amount' : amount,
               'table_contents' : investments}
    return render(request, 'track/index.html', context)

