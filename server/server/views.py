from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .api_query import get_trend_data
import os


@csrf_exempt
def getlist(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        print('keyword: %s' % keyword)
        data = get_trend_data(keyword)
        a = []
        for key, dict in data.items():
            sum = 0
            for year, num in dict.items():
                sum += num
            a.append((sum, key))
        a.sort(reverse=True)
        a = [x[1] for x in a]
        print('return %d items' % len(a))
        return HttpResponse(json.dumps(a))


def getfig1(request):
    file = open('./server/hype_cycle.bmp', 'rb')
    data = file.read()
    return HttpResponse(data, content_type='image/png')
