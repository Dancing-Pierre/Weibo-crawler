import re
import requests
import json
import csv

headers = {
    "cookie": "_T_WM=38765301285; XSRF-TOKEN=e98df6; WEIBOCN_FROM=1110006030; MLOGIN=0; mweibo_short_token=8dbf74ac31; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D3%2526q%253D%25E5%258C%25BB%25E7%25BE%258E%2526t%253D%26fid%3D100103type%253D1%2526q%253D%25E5%258C%25BB%25E7%25BE%258E%26uicode%3D10000011",
    "mweibo-pwa": "1",
    "referer": "https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E5%8C%BB%E7%BE%8E",
    "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrf-token": "e98df6"
}
csv_obj = open('yuanshuju.csv', 'w', encoding='gb18030', newline='')
csv.writer(csv_obj).writerow(["用户名", "url", "简介", "粉丝"])

for i in range(3, 8):
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D3%26q%3D%E5%8C%BB%E7%BE%8E%26t%3D&page_type=searchall&page='+str(i)
    response = requests.get(url=url, headers=headers)
    data = response.text
    content_dict = json.loads(data)
    # print(content_dict)
    post_list = content_dict['data']['cards']#[1]['card_group']
    # print(post_list)
    for value_dict in post_list:
        post_list = value_dict['card_group']
        for v in post_list:
            id = v['user']['screen_name']
            link = v['user']['profile_url']
            detail = v['user']['description']
            fun = v['user']['followers_count']
            # funs = re.findall('(?<=：).*', fun)
            csv.writer(csv_obj).writerow([id, link, detail, fun])
        print("第" + str(i) + "页爬取完成")
csv_obj.close()
