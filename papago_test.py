# 다른 API를 이용하려면 requests 라이브러리를 이용하면된다


import requests

URL = 'https://openapi.naver.com/v1/papago/n2mt'

client_id = 'Djidio5sW87iKVCzshZE'
cliemt_secret = 'qYBBvvXBZO'

headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8' , 'X-Naver-Client-Id' : client_id ,'X-Naver-Client-Secret': cliemt_secret }


data = {'source' : 'ko' , 'target' : 'zh-CN' , 'text' :'만나서 반갑습니다'}

res = requests.post(URL , data , headers= headers)

print(res.json())
