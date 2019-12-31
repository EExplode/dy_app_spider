import urllib.request
import json
import os

path = 'C:\\Users\\only\\Desktop\\video\\'
url_key = '/aweme/v1/aweme/post'


def response(flow):
    if url_key in flow.request.url:
        print("hello\n" * 3)
        data = json.loads(flow.response.text)  # 以json方式加载response
        u_id = data['aweme_list'][0]['author']['uid']  # 用户ID，不可见
        unique_id = data['aweme_list'][0]['author']['unique_id']  # 抖音号
        u_name = data['aweme_list'][0]['author']['nickname']  # 昵称
        #  以用户ID为目录，判断用户ID，不下载重复文件
        user_path = path + u_id
        if not os.path.exists(user_path):
            os.mkdir(user_path)
            # os.makedirs(user_path)
            num = 1
            for data in data['aweme_list']:
                video_name = data['desc'] or data['aweme_id']  # 视频描述或视频ID，作为文件名
                video_url = data['video']['play_addr']['url_list'][0]  # 视频链接
                filename = user_path + '\\' + video_name
                urllib.request.urlretrieve(video_url, filename=filename + '.mp4')
                print('下载完成：' + filename)
                if num < 2:
                    num += 1
                else:
                    break
