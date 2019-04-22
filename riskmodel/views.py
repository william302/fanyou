from django.shortcuts import render
from .tongdun import get_tongdun_res
from django.http import HttpResponse
from .sql import insert_userbase
from .query import final_decision_chart, risk_item_chart
import json
# Create your views here.


def index(request):
    data = {}
    re = final_decision_chart()
    fd = [d[0] for d in re]
    count = [d[1] for d in re]
    data['fd'] = fd
    data['count'] = count
    return render(request, 'riskmodel/index.html', {'data': json.dumps(data)})


def risk_item(request):
    data = {}
    re = risk_item_chart()
    data['rn'] = [d[0] for d in re]
    data['count'] = [d[1] for d in re]
    return render(request, 'riskmodel/risk_item.html', {'data': json.dumps(data)})


def start(request):
    l = ['邓传森', 18820843664, '360732199111171753']

    # result = json.loads(result)
    result = get_tongdun_res(l)
    insert_userbase(l[0], l[1], l[2], result)
    return HttpResponse('success')