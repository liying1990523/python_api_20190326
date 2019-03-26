import requests
data = {'mobilephone':'18566743962','pwd':'123456'}
resp = requests.post('http://192.168.108.175:8080/futureloan/mvc/api/member/register',data=data)
print('响应码',resp.status_code)
print('响应信息：',resp.text)