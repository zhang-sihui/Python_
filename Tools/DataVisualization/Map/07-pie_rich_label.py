# @Author: zhang
# @Python -v 3.7.3
# @time: 2019/7/26 13:03

import json
from pyecharts import options as opts
from pyecharts.charts import Pie

with open('./data/pie_data.json','r',encoding='utf-8') as f:
    data = json.load(f)

value_list = []
for a_dict in data:  # 遍历数据列表
    for _, value in a_dict.items():  # 获取字典的值
        value_list.append(value)
value_num = value_list[::2]  # 获取列表中从0开始每两个取一次的数据
value_str = value_list[1::2]  # 获取列表中从1开始每两个取一次的数据

def pie_rich_label() -> Pie:
    pie_map = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(value_str,value_num)],  # 数据
            radius=["40%", "55%"],  # 设置内圆半径和外圆半径
            label_opts=opts.LabelOpts(   # 标签设置
                position="outside",    # 标签的位置
                # 标签内容格式器，支持字符串模板和回调函数两种形式，
                # 字符串模板与回调函数返回的字符串均支持用 \n 换行。
                # 示例：formatter: '{b}: {@score}' .  参考官网
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={  # 在 rich 里面，可以自定义富文本样式。利用富文本样式，可以在标签中做出非常丰富的效果
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-富文本示例",  # 标题及位置
                                                   pos_top = '450'))
    )
    pie_map.width = '1000px'
    pie_map.height = '600px'
    pie_map.render('./data/pie_rich_label.html')

pie_rich_label()
