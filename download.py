import requests
from bs4 import BeautifulSoup
import json

vid = 'BV1os411D7be'
# vid = 'BV1Q3411Y7Z6'

if __name__ == "__main__":
    video_info = requests.get("https://api.bilibili.com/x/player/pagelist?bvid="+vid+"&jsonp=jsonp")
    video_info = BeautifulSoup(video_info.text, "html.parser")
    video_info_json = json.loads(video_info.text)
    cid = video_info_json['data'][0]['cid']

    barrage_info = requests.get("https://api.bilibili.com/x/v1/dm/list.so?oid="+str(cid))
    barrage_info.encoding = 'utf-8'
    # print(barrage_info.text)
    barrage_info = BeautifulSoup(barrage_info.text, "xml")
    barrages = barrage_info.find_all('d')
    for barrage in barrages:
        # print(barrage['p'],barrage.get_text())
        single_barrage_info = barrage['p'].split(',')
        single_barrage_text = barrage.get_text()
        print(single_barrage_info[0],single_barrage_text)