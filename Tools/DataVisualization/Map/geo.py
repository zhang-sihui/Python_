# @Author: zhang
# @time: 2019/7/18 14:05

from pyecharts import options as opts
from pyecharts.charts import Geo, Page
from pyecharts.globals import ChartType, SymbolType

# 定义地理图
geo = Geo()
# 画布宽度,高度
geo.width = '800px'
geo.height = '600px'
# 全局设置
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=100),
                    title_opts=opts.TitleOpts(title='Geo-流向图'))
# 添加主题，中国地图，填充边界颜色
geo.add_schema(maptype='china',
               itemstyle_opts=opts.ItemStyleOpts(border_color="#111",
                                                 color='#454545')
               )
# 添加系列
geo.add('',
        [('成都',10),('武汉',20),('西安',30),('南京',40),('深圳',50)],
        type_=ChartType.EFFECT_SCATTER,   # 散点图一种形式
        label_opts=opts.LabelOpts(is_show=True),  # 不显示设置False
        )
geo.add('',
        [('北京',100),('上海',100)],
        type_=ChartType.HEATMAP,    # 散点图的一种形式
        label_opts=opts.LabelOpts(is_show=False),
       )

# 设置流向
geo.add('流向图',
        [('上海','成都'),('上海','南京'),('上海','深圳'),('上海','武汉'),
         ('北京','西安'),('北京','成都'),('北京','南京'),('北京','武汉')],
        type_=ChartType.LINES,
        linestyle_opts=opts.LineStyleOpts(curve=0.3,color="#63B8FF"),
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                    symbol_size=6,
                                    color='#FF7F00'),
        )

# 生成图片
geo.render('./data/geo_liuxiang.html')