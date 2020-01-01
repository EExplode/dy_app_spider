import json
from bs4 import BeautifulSoup
import re
import pymongo

# TypeError: MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True) is not a callable object
client = pymongo.MongoClient('localhost')
db = client['jd']
comments_collection = db['comments']
products_collection = db['products']

# 商品评价API，返回json数据类型
url_1 = 'https://api.m.jd.com/client.action?functionId=getCommentListWithCard'
url_2 = 'https://111.13.149.100/client.action?functionId=getCommentListWithCard'

# 商品详情API，返回HTML数据类型
url_3 = 'https://in.m.jd.com/product/detail'


def response(flow):
    if url_1 in flow.request.url or url_2 in flow.request.url:
        text = flow.response.text
        data = json.loads(text)
        comments = data.get('commentInfoList')
        for comment in comments:
            if comment.get('commentInfo') and comment.get('commentInfo').get('commentData'):
                info = comment.get('commentInfo')
                nick_name = info.get('userNickName')
                comment_id = info.get('commentId')
                text = info.get('commentData')
                time = info.get('commentDate')
                print(nick_name)
                print(comment_id)
                print(text)
                print(time, end='\n\n\n')

                comments_collection.insert({
                    'nick_name': nick_name,
                    'text': text,
                    'time': time
                })

    if url_3 in flow.request.url:
        soup = BeautifulSoup(flow.response.text, 'lxml')
        product_info = soup.find(name='input', attrs={'id': 'wareGuigNew'})['value']

        product_id = soup.find(name='input', attrs={'id': 'wareId'})['value']
        product_name = re.search('.*?\{"产品名称":"(.*?)"\}.*?', product_info).group(1)
        time_to_market = re.search('.*?\{"上市年份":"(.*?)"\}.*?', product_info).group(1)
        if re.search('.*?\{"品牌":"(.*?)"\}.*?', product_info):
            brand = re.search('.*?\{"品牌":"(.*?)"\}.*?', product_info).group(1)
        else:
            brand = '杂牌'
        print(product_info)
        print(product_name)
        print(brand)
        print(time_to_market, end='\n\n\n')

        products_collection.insert({
            'product_id': product_id,
            'product_name': product_name,
            'brand': brand,
            'time_to_market': time_to_market
        })
