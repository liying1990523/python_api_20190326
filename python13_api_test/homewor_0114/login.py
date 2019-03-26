import requests
data = {'mobilephone':'18566743962','pwd':'123456'}
resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login',params=data)
print('响应码',resp.status_code)
print('响应信息：',resp.text)