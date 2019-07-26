# @Author: zhang
# @Python -v 3.7.3
# @time: 2019/7/25 21:53

from example.commons import Faker  # pyecharts中自带的例子数据
from pyecharts import options as opts
from pyecharts.charts import Page, Pie

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

value_list = []
for a_dict in data:  # 遍历数据列表
    for _, value in a_dict.items():  # 获取字典的值
        value_list.append(value)
value_num = value_list[::2]  # 获取列表中从0开始每两个取一次的数据
value_str = value_list[1::2]  # 获取列表中从1开始每两个取一次的数据


def pie_base():
    piemap = (
        Pie()
            # .add('',[list(z) for z in zip(Faker.choose(), Faker.values())])  #  pyecharts自带的例子
            .add('', [list(z) for z in zip(value_str, value_num)],  # 数据格式:[(a,b),(c,d),]
                 center=["50%","60%"]  # 饼图位置
                 )
            .set_global_opts(title_opts=opts.TitleOpts(title='Pie-饼图', pos_top='100'))  # 标题及位置
            .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}'))  # 标签及格式
    )
    piemap.width = '1000px'  # 图宽
    piemap.height = '600px'  # 图高
    piemap.render('./data/piemap.html')  # 存储

pie_base()
