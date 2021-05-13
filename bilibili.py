# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:14:41 2019

@author: trh
"""
def get_data(video_owner_url):
    #Refer = 'Referer: https://www.bilibili.com/video/av38343727/?spm_id_from=333.788.videocard.3'
    video_owner_data = json.loads(session.get(video_owner_url).text)
    video_name = video_owner_data['data']['title']#视频名字
    video_owner_mid = video_owner_data['data']['owner']['mid']#up主id
    video_owner_name = video_owner_data['data']['owner']['name']#up主名字
    video_av = video_owner_data['data']['stat']['aid']#视频av号
    video_view = video_owner_data['data']['stat']['view']#播放量
    video_danmaku = video_owner_data['data']['stat']['danmaku']#弹幕
    video_coin = video_owner_data['data']['stat']['coin']#投币
    video_favorite = video_owner_data['data']['stat']['favorite']#收藏
    video_share = video_owner_data['data']['stat']['share'] #分享
    video_like = video_owner_data['data']['stat']['like']#点赞
    print('视频名称：'+ video_name)
    print('视频av: '+ str(video_av))
    print('up主id: '+ str(video_owner_mid))
    print('up主名字: '+ video_owner_name)
    print('播放量: '+ str(video_view))
    print('弹幕数: '+ str(video_danmaku))
    print('投币数: '+ str(video_coin))
    print('点赞数: '+ str(video_like))
    print('收藏: '+ str(video_favorite))
    print('分享:'+ str(video_share))
import requests
#import os
import json
import urllib
#from lxml import etree
#from PIL import Image
if __name__=='__main__':
    session = requests.session()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    video_owner_url = 'https://api.bilibili.com/x/web-interface/view?aid=38343727&cid=67399378'
    get_data(video_owner_url)
    
    #html_url = 'https://www.bilibili.com/video/av79432204?spm_id_from=333.851.b_7265706f7274466972737432.5'
    #req = urllib.request.Request(url=html_url, headers=headers)  
    #html_data = urllib.request.urlopen(req).read().decode('utf-8')
    #print(html_data)
    