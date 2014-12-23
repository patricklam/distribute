from django.shortcuts import render

def index(request):
    # amount = request.POST['amount']
    context = {'table_contents' : '<tr><td>foo</td></tr>'}
    return render(request, 'track/index.html', context)

