from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .api_query import get_trend_data


@csrf_exempt
def getlist(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        print('keyword: %s' % keyword)
        data = get_trend_data(keyword)
        a = [key for key in data]
        print('return %d items' % len(a))
        return HttpResponse(json.dumps(a))
