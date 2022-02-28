from matplotlib.pyplot import bar
import requests
from bs4 import BeautifulSoup
import json

bvid = 'BV1os411D7be'
# bvid = 'BV1Q3411Y7Z6'

def get_video_cid(bvid):
    video_info = requests.get("https://api.bilibili.com/x/player/pagelist?bvid="+bvid+"&jsonp=jsonp")
    print('get cid',video_info.status_code)
    video_info = BeautifulSoup(video_info.text, "html.parser")
    video_info_json = json.loads(video_info.text)
    cid = video_info_json['data'][0]['cid']
    return cid

def get_barrage(cid):
    barrage_info = requests.get("https://api.bilibili.com/x/v1/dm/list.so?oid="+str(cid))
    print('get barrage',barrage_info.status_code)
    barrage_info.encoding = 'utf-8'
    barrage_info = BeautifulSoup(barrage_info.text, "xml")
    # print(barrage_info)
    barrages = barrage_info.find_all('d')
    result = []
    for barrage in barrages:
        # print(barrage['p'],barrage.get_text())
        single_barrage_info = barrage['p'].split(',')
        single_barrage_text = barrage.get_text()
        result.append([single_barrage_info[0],single_barrage_text])
    return result

def save_barrage(bvid,barrage):
    with open(bvid+'_barrage.txt','w') as file:
        for single_barrage in barrage:
            file.write(single_barrage[0]+' "'+single_barrage[1]+'"\n')
    return

if __name__ == "__main__":
    cid = get_video_cid(bvid)
    print('cid : ',cid)
    barrage = get_barrage(cid)
    save_barrage(bvid,barrage)

    