# coding=utf-8
import requests
import time
import json
import pymongo

def parse_page():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3',
        'Referer': 'https://www.lagou.com/jobs/list_'+name+'?labelWords=&fromSearch=true&suginput=',
        'Accept': 'application/json, text/javascript, */*; q=0.01'
    }
    url_start = 'https://www.lagou.com/jobs/list_'+name+'?labelWords=&fromSearch=true&suginput='
    url_parse = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    #连接mongodb
    myclient = pymongo.MongoClient('192.168.1.107', 27017)
    #创建数据库test
    mydb = myclient["final"]
    dblist = myclient.list_database_names()
    #创建集合name
    mycol = mydb['java']
    collist = mydb.list_collection_names()

    for x in range(1, 30):
        data = {
            ' first': 'true',
            'pn': str(x),
            'kd': name
        }
        s = requests.Session()  #会话维持
        s.get(url_start, headers=headers, timeout=3)
        cookie = s.cookies
        res = requests.post(url_parse, headers=headers, cookies=cookie, data=data, timeout=3)
        time.sleep(2)
        res.encoding = res.apparent_encoding #apparent_endoding可以根据网页内容分析出编码方式，比encoding更加准确
        result = json.loads(res.text)
        info = result["content"]["positionResult"]["result"]
        for i in info:
            technique_list=i['positionLables']
            technique=''
            if len(technique_list):
                for j in  technique_list:
                    technique+=j+','
                    # 保存到MongoDB中
            try:
                if mycol.insert_one({'job': i['positionName'], 'experience': i['workYear'], 'zone': i['city'], 'salary': i['salary'], 'major': i['education'],'ability':technique}):
                    print("存储成功")
            except Exception:
                print("存储失败")



if __name__ == '__main__':
    name = input('请输入想要爬取的内容：')
    parse_page()
