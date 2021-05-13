# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import requests
import os
import json
from PIL import Image


def get_captcha():
    captcha_url = "http://jwxs.tjpu.edu.cn/img/captcha.jpg"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
            f.write(r.content)
            f.close()
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


def register(study_year, frequency):
    global cookie, cookie_jar
    post_url = "http://jwxs.tjpu.edu.cn/j_spring_security_check"
    data_url = 'http://jwxs.tjpu.edu.cn/student/integratedQuery/scoreQuery/allTermScores/data'
    postdata = {
            'j_username': 'xxx',
            'j_password': 'xxx',
            'j_captcha': '',
            }
    if frequency == 0:
        postdata["j_captcha"] = get_captcha()
        register_page = session.post(post_url, data=postdata, headers=headers)
        print(register_page.status_code)
    postdata = {
            'zxjxjhh': study_year,
            'kch': '',
            'kcm': '',
            'pageNum': 1,
            'pageSize': '30',
            }
    if frequency == 0:
        data = session.post(data_url, data=postdata, headers=headers)
        cookie_jar = session.post(data_url, data=postdata, headers=headers).cookies
        cookie = requests.utils.dict_from_cookiejar(cookie_jar)
    if frequency > 0:
        # data = session.post(data_url, data = postdata, headers = headers, cookies = cookie)
        data = session.post(data_url, data=postdata, headers=headers)
    # print(data.text)
    json_data = json.loads(data.text)
    comment_list = json_data['list']['records']
    grade = {}
    for eachone in comment_list:
        if eachone[11] in grade:
            grade[eachone[11]] = max(grade[eachone[11]], eachone[8])
        else:
            grade[eachone[11]] = eachone[8]
        print(eachone[11], grade[eachone[11]])
        # with open('data.txt','w') as f1:
        #    f1.write(grade)
        #   f1.close()
    return grade


if __name__ == '__main__':
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    headers = {
            'Host': 'jwxs.tjpu.edu.cn',
            'Origin': 'http://jwxs.tjpu.edu.cn',
            'Referer': 'http://jwxs.tjpu.edu.cn/login',
            'User-Agent': agent,
            }
    global cookie, cookie_jar
    frequency = 0
    study_year_list = ['2019-2020-1-1', '2018-2019-2-1', '2018-2019-1-1', '2017-2018-2-1', '2017-2018-1-1']
    while(1):
        print('2019-2020秋--1\n2018-2019春--2\n2018-2019秋--3\n2017-2018春--4\n2017-2018秋--5\n')
        number = input('Please enter the amount you want to query the number of school year.\n>')
        session = requests.session()
        grade = register(study_year_list[int(number)-1], frequency)
        frequency = frequency + 1
