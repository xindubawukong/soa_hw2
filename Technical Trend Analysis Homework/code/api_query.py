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
    print(term_freq)
    return term_freq

if __name__ == '__main__':
    get_trend_data('大数据')