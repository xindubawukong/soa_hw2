import requests
import json
from urllib.parse import quote

session = requests.Session()
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'


def get_trend_data(field):
    headers = {'User-Agent': USER_AGENT, 'Referer': 'http://trend.aminer.cn/topic/trend?query='+quote(field), 'Origin': 'http://trend.aminer.cn', 'Content-Type': 'Content-Type:application/json'}
    url = 'https://apiv2.aminer.cn/magic?a=getTrend__trend.GenTrend___'
    data = [{"action": "trend.GenTrend", "parameters": {"query": field, "size": 11, "searchType": "all", "advquery": {"texts": [{"source": "start_year", "text": "2000"}, {"source": "end_year", "text": "2017"},{"source": "isReload", "text": "false"}]}}, "schema": {"person": ["id", "name", "profile.org"]}}]
    res = session.post(url, data=json.dumps(data), headers=headers)
    term_freq = json.loads(res.text)['data'][0]['items'][0]['data']['term_freq_by_year']
    return term_freq


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle
    import io
    import cv2
    data = get_trend_data('大数据')
    print(data)
    a = []
    for key, dict in data.items():
        sum = 0
        for year, num in dict.items():
            sum += num
        a.append((sum, key, dict))
    a.sort(reverse=True)
    data = a
    print(data)
    from hype_cycle import get_pos, get_XY
    X, Y = get_XY()
    figure = plt.figure(figsize=(18, 8))
    plt.plot(X, Y)
    for x in data[:20]:
        vector = []
        for year, num in x[2].items():
            vector.append(num)
        pos = get_pos(vector)
        print(pos)
        plt.text(pos[0][0] - 0.002, pos[0][1] - 0.002, 'o')
        plt.annotate(s=x[1], xy=(pos[0][0], pos[0][1]), xytext=(pos[0][0] + 0.05, pos[0][1]), arrowprops={'arrowstyle': '->'})
    plt.show()
