"""
@function：定义常量，主要是文件路径
"""
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根路径
# print(base_dir)

# datas文件夹中相关文件的路径
data_dir = os.path.join(base_dir, "datas")  # datas文件夹路径
case_file = os.path.join(data_dir, "cases.xlsx") # case.xlsx文件路径
# print(case_file)
recharge_cases = os.path.join(data_dir, "recharge_cases.xlsx") # recharge_cases.xlsx文件路径

# conf文件夹中相关文件的路径
conf_dir = os.path.join(base_dir, "conf") # conf文件夹路径
global_conf = os.path.join(conf_dir, "global.conf") # global.conf文件路径
test_conf = os.path.join(conf_dir, "test.conf") # test.conf文件路径
test2_conf = os.path.join(conf_dir, "test2.conf") # test2.conf文件路径

# logs日志文件路径
logs_dir = os.path.join(base_dir,'logs')

# testcases测试用例目录
testcases_dir = os.path.join(base_dir,'testcases')

#reports测试报告目录
reports_dir = os.path.join(base_dir,'reports')
report_html = os.path.join(reports_dir,'reports.html')