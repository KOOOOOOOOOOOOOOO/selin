# -*- coding: utf-8 -*-
"""Colaboratory에 오신 것을 환영합니다

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/welcome.ipynb
"""

from google.colab import files
myfile = files.upload()

import numpy as np#웹스크래핑전 전처리 과정
import pandas as pd#엑셀 파일 받아와서 필요한 정보로만 정리

code_df = pd.read_csv('/content/여수시 법정동명 - Sheet2.csv')
code_df.head()

code_df['폐지여부'].value_counts()

code_df = code_df[code_df['폐지여부'] == '존재']
code_df.head()

code_df.to_excel('Test.xlsx')

gj_df = pd.read_excel('/content/여수시 법정동명.xlsx')
gj_df.head()

import bs4, requests
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode, quote_plus

service_code = '1BbTDShpnMbdfJuw6kW7qfL%2F29oW%2FtjFKlEMHOn82x6bd%2FZbGFgyCYSilUJvn74Hzcw13LqswIomhKy5YOywqQ%3D%3D'
apt_name = []
apt_dict = {'법정동코드':[],
           '법정동명':[],
            '아파트명':[],
           }

bjd_code = list(gj_df['법정동코드'])
bjd_name = list(gj_df['법정동명'])

for i in range(len(bjd_code)):
    url = 'http://apis.data.go.kr/1613000/AptListService1/getLegaldongAptList?' + 'bjdCode=' + str(bjd_code[i]) + '&ServiceKey=' + service_code 
    response = requests.get(url).text.encode('utf-8')
    response_body = bs4.BeautifulSoup(response, 'lxml-xml')
    tmp = response_body.findAll('kaptName')
    if len(tmp) == 0:
        continue
    for j in range(len(tmp)):
        apt_name.append(tmp[j].get_text())
    for k in apt_name:
        apt_dict['법정동코드'].append(str(bjd_code[i]))
        apt_dict['법정동명'].append(bjd_name[i])
        apt_dict['아파트명'].append(k)


apt_df = pd.DataFrame(apt_dict)
apt_df.head()
apt_df.to_excel('apt_여수.xlsx')

data = pd.read_csv(io.BytesIO(myfile['train 2.csv']))
data.head()