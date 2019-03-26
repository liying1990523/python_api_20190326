import requests
data = {'mobilephone': '15810447656', 'pwd': '123456'}
resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login',data=data)
print(resp.text)
resp_cookies = resp.cookies
data_recharg = {'mobilephone':'15810447656','amount':'10000'}
resp_recharge = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/recharge',data=data_recharg,cookies=resp_cookies)
print('响应码',resp_recharge.status_code)
print('响应信息：',resp_recharge.text)