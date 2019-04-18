from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def getlist(request):
    if request.method == 'POST':
        print(request.POST.get('keyword'))
        return HttpResponse(json.dumps('asd'))
