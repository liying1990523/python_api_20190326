"""
@function：request封装类来完成get，post的请求
"""
import requests
import json
from common.config import ReadConfig
from common import logger

logger = logger.get_logger('request')
class Request:
    def __init__(self):
        self.session = requests.sessions.session()  # 实例化一个session

    def request(self, method, url, data=None):
        method = method.upper()  # 将字符串全部转化成大写
        if data is not None and type(data) == str:  # 从表格中读取的data是字符串类型，而request里需要字典
            data = eval(data)  # 将字符串转化成字典
            # data = json.loads(data) #将json格式的字符串转化为字典
        logger.info('url: {0}'.format(url))
        config = ReadConfig()
        pre_url = config.get('api', 'pre_url')
        url = pre_url + url  #URL拼接
        logger.info('method: {0}  拼接后url: {1}'.format(method, url))
        logger.info('data: {0}'.format(data))
        # print('data: {0}'.format(data),type(data))
        if method == 'GET':
            resp = self.session.request(method, url=url, params=data)  # 调用get方法，使用params传参
            logger.info('response: {0}'.format(resp.text))
            return resp
        elif method == 'POST':
            resp = self.session.request(method, url=url, data=data)  # 调用post方法，使用data传参
            logger.info('response: {0}'.format(resp.text))
            return resp
        else:
            logger.error('Un-support method !!!')

    def close(self):
        self.session.close()  # 关闭session


if __name__ == '__main__':
    re = Request()
    from common.do_excel import DoExcel
    from common import constants

    do_excel = DoExcel(constants.case_file)
    cases = do_excel.get_cases('login')
    # data = '{"mobilephone": "18566743962", "pwd": null}'
    # url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    # resp = re.request('get',url,data)
    # print(resp.status_code)
    for case in cases:
        resp = re.request(case.method, case.url, case.data)
        print(resp.text)
