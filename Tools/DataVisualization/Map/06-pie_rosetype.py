# @Author: zhang
# @Python -v 3.7.3
# @time: 2019/7/26 10:14

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

def pie_rosetype() -> Pie:
    piemap = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(value_str, value_num)],
            radius=["30%", "75%"],  # 图的内圆半径和外圆半径
            center=["20%", "50%"],  # 图的位置占屏幕比例，相对宽度和高度
            rosetype="radius",  # radius：扇区圆心角展现数据的百分比，半径展现数据的大小
                                # area：所有扇区圆心角相同，仅通过半径展现数据大小
            label_opts=opts.LabelOpts(is_show=False),  # 是否展示标签
        )
        .add(
            "",
            # 系列数据项，格式为 [(key1, value1), (key2, value2)]
            [list(z) for z in zip(value_str, value_num)],
            radius=["30%", "75%"],
            center=["70%", "50%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图",  # 标题及位置
                                                   pos_top='500'))
    )
    piemap.width = '1100px'
    piemap.height = '600px'
    piemap.render('./data/pie_rosetype.html')  # 存储

pie_rosetype()