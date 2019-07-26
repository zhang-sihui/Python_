# @Author: zhang
# @Python -v 3.7.3
# @time: 2019/7/26 17:26

import json
from pyecharts import options as opts
from pyecharts.charts import Sunburst

def sunburst_official() -> Sunburst:
    with open("./data/sun_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    sun_map = (
        Sunburst(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(
            "",
            data_pair=data,  # 数据Sequence
            highlight_policy="ancestor",  # 当鼠标移动到一个扇形块时，可以高亮相关的扇形块。
                                          # 'ancestor'：高亮该扇形块和祖先元素
            radius=[0, "95%"],  # 图的半径,第一项是内半径，第二项是外半径
            sort_="null",  # # 扇形块根据数据 value 的排序方式，
                           # 如果未指定 value，则其值为子元素 value 之和。
                           # 'null'：表示不排序，使用原始数据的顺序
            levels=[    # 图多层级配置
                {},
                {
                    "r0": "15%",
                    "r": "35%",
                    "itemStyle": {"borderWidth": 2},
                    "label": {"rotate": "tangential"},
                },
                {"r0": "35%", "r": "70%", "label": {"align": "right"}},
                {
                    "r0": "70%",
                    "r": "72%",
                    "label": {"position": "outside", "padding": 3, "silent": False},
                    "itemStyle": {"borderWidth": 3},
                },
            ],
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Sunburst-示例"))
            # 标签内容格式器，支持字符串模板和回调函数两种形式，
            # 字符串模板与回调函数返回的字符串均支持用 \n 换行。
            # 示例：formatter: '{b}: {@score}' .  参考官网
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    )
    sun_map.render('./data/sun_map.html')

sunburst_official()
