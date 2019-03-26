'''
HTTP协议两大部分：Request Response
Request:
1、请求方法：
get 查--获取资源
post 改--修改资源  或者 新增
put 新增
delete 删除
option 获取可以支持的请求方式
header 返回请求和响应的头部信息，没有返回体
2、请求URL: 协议://服务器IP地址:端口号/接口路径
3、请求参数：传参方式：URL传参、表单
4、header请求头：Content-type  User-Agent(请求端信息)
5、cookie 服务器端返回的，放在客户端，保存到本地，下次请求需要带着的标识

Response：
1、状态码：
1XX	信息性类（Information）	表示收到web浏览器的请求，正在进一步的处理中
2XX	成功类（Successful）	表示用户请求被正确接收、理解和处理
3XX	重定向类（Redirection）	表示请求没有成功，客户必须采取进一步的动作，需要进行额外操作以完成请求
4XX	客户端错误（Client Error）	表示客户端提交的请求有错误
5XX	服务器错误（Server Error）	表示服务器不能完成对请求的处理
2、响应信息
3、cookie
4、header：Content-type
'''
import requests
# req = requests.get('http://cn.python-requests.org/zh_CN/latest/')
# req.encoding='utf-8'
# print(req.status_code)
# print(req.text)
# # with open('index.html','wb') as file:
# #     file.write(req.content)
# with open('index_txt.html','w+',encoding='utf-8') as file:
#     file.write(req.text)
data = {'mobilephone':'15810447656','pwd':'123456'}
# get--url传参--使用params
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login',params=data)
# post--表单传参--使用data
resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login',data=data)
print('请求URL：',resp.request.url)
print('请求参数：',resp.request.body)
print('请求的headers',resp.request.headers)
print('请求的cookies',resp.request._cookies)
print('响应的状态码：',resp.status_code)
print('响应信息：',resp.text)
print('响应的headers',resp.headers)
print('响应的cookies',resp.cookies)
# requests中response.json()方法等同于json.loads（response.text）方法
print('响应信息：',resp.json())
print(type(resp.json()))
print('响应信息msg：',resp.json()['msg'])
