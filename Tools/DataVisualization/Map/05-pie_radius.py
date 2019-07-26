# @Author: zhang
# @time: 2019/7/26 9:26
# @Python -v 3.7.3
# @pyecharts -v1.3.1


import json
from pyecharts import options as opts
from pyecharts.charts import Page, Pie

with open('./data/pie_data.json', 'r',encoding='utf-8') as f:
    data = json.load(f)

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
                 center=["50%","60%"],   # 饼图位置
                 radius=['40%','75%'])   # 设置内圆半径和外圆半径
            .set_global_opts(title_opts=opts.TitleOpts(title='Pie-圆环饼图', pos_top='100'))  # 标题及位置
            .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}'))  # 标签及格式
    )
    piemap.width = '1000px'  # 图宽
    piemap.height = '600px'  # 图高
    piemap.render('./data/pie_radius.html')  # 存储

pie_base()
