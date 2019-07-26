# @Author: zhang
# @Python -v 3.7.3
# @time: 2019/7/26 9:30
import json

"""
将列表（字典\字符串...）数据转换为Json格式数据

"""

data = [
    {'value': 20, 'name': '计算机与信息工程学院'},
    {'value': 12, 'name': '物理与电子科学学院'},
    {'value': 17, 'name': '政法与公共管理学院'},
    {'value': 21, 'name': '材料科学与工程学院'},
    {'value': 59, 'name': '数学与统计学学院'},
    {'value': 22, 'name': '马克思主义学院'},
    {'value': 9, 'name': '资源环境学院'},
    {'value': 18, 'name': '生命科学学院'},
    {'value': 16, 'name': '化学化工学院'},
    {'value': 22, 'name': '历史文化学院'},
    {'value': 29, 'name': '外国语学院'},
    {'value': 34, 'name': '教育学院'},
    {'value': 20, 'name': '文学院'},
    {'value': 6, 'name': '商学院'},
]

with open('./data/pie_data.json','w',encoding='UTF-8') as f:
    # 设置ensure_ascii=False，确保中文不乱码
    json.dump(data,f,ensure_ascii=False)  # 设置ensure_ascii=False，确保中文不乱码
