from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .api_query import get_trend_data
from .hype_cycle import get_XY, get_pos
import matplotlib.pyplot as plt
import io
import os


data = []


@csrf_exempt
def getlist(request):
    global data
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        print('keyword: %s' % keyword)
        data = get_trend_data(keyword)
        a = []
        for key, dict in data.items():
            sum = 0
            for year, num in dict.items():
                sum += num
            a.append((sum, key, dict))
        a.sort(reverse=True)
        data = a
        a = [x[1] for x in data]
        print('return %d items' % len(a))
        return HttpResponse(json.dumps(a))


@csrf_exempt
def getfig(request):
    global data
    file = open('./server/hype_cycle.bmp', 'rb')
    res = file.read()
    plt.switch_backend('agg')
    figure = plt.figure(figsize=(18, 8))
    plt.title('Hotspot Map of Year')
    for i in range(10):
        x = []
        y = []
        for year, num in data[i][2].items():
            x.append(int(year))
            y.append(num)
        plt.plot(x, y)
    legend = [x[1] for x in data]
    plt.legend(legend)
    plt.xlim(2000, 2017)

    canvas = figure.canvas
    buffer = io.BytesIO()
    canvas.print_png(buffer)
    res2 = buffer.getvalue()
    buffer.close()
    return HttpResponse(res2, content_type='image/png')


@csrf_exempt
def getxy(request):
    global data
    X, Y = get_XY()
    pos = []
    for x in data[:20]:
        vector = []
        for year, num in x[2].items():
            vector.append(num)
        p = get_pos(vector)
        pos.append((p[0][0], p[0][1], x[1]))
    res = [X, Y, pos]
    return HttpResponse(json.dumps(res))
