# @Author: zhang
# @time: 2019/7/18 15:33
# @ Python -v3.7.3
# @ pyecharts -v1.3.1


from pyecharts.charts import TreeMap
from pyecharts import options as opts

# 数据
data = [
    {'value': 20,
     'name': '计算机与信息工程学院',
     'children': [
         {'value': '7', 'name': '软件工程'},
         {'value': '3', 'name': '软件工程产业 '},
         {'value': '3', 'name': '信息安全 '},
         {'value': '2', 'name': '通信工程 '},
         {'value': '2', 'name': '通信工程产业 '},
         {'value': '2', 'name': '计算机科学与技术'},
         {'value': '1', 'name': '电子信息工程 '}]},

    {'value': 12,
     'name': '物理与电子科学学院',
     'children': [
         {'value': '2', 'name': '物理学 '},
         {'value': '1', 'name': '光电信息与工程 '},
         {'value': '3', 'name': '微电子科学与工程'},
         {'value': '6', 'name': '电子科学与技术 '}
     ]},

    {'value': 17,
     'name': '政法与公共管理学院',
     'children': [
         {'value': '5', 'name': '法学 '},
         {'value': '8', 'name': '公共管理类 '},
         {'value': '4', 'name': '电子商务及法律 '}
     ]},

    {'value': 21,
     'name': '材料科学与工程学院',
     'children': [
         {'value': '4', 'name': '材料化学 '},
         {'value': '1', 'name': '材料物理 '},
         {'value': '11', 'name': '高分子材料与工程'},
         {'value': '3', 'name': '新能源材料与器件'},
         {'value': '2', 'name': '无机非金属材料 '}
     ]},

    {'value': 59,
     'name': '数学与统计学学院',
     'children': [
         {'value': '35', 'name': '数学与应用数学 '},
         {'value': '18', 'name': '信息与计算科学 '},
         {'value': '6 ', 'name': '应用统计学 '}
     ]},

    {'value': 22,
     'name': '马克思主义学院',
     'children': [
         {'value': '22', 'name': '思想政治教育 '},
     ]},

    {'value': 9,
     'name': '资源环境学院',
     'children': [
         {'value': '2', 'name': '地理科学 '},
         {'value': '3', 'name': '地理信息科学 '},
         {'value': '1', 'name': '环境类 '},
         {'value': '1', 'name': '环境工程 '},
         {'value': '2', 'name': '人文地理与城乡规划'}
     ]},

    {'value': 18,
     'name': '生命科学学院',
     'children': [
         {'value': '5', 'name': '生物科学试点班 '},
         {'value': '5', 'name': '生物技术 '},
         {'value': '5', 'name': '药学 '},
         {'value': '3', 'name': '生物工程 '}
     ]},

    {'value': 16,
     'name': '化学化工学院',
     'children': [
         {'value': '9', 'name': '应用化学 '},
         {'value': '1', 'name': '应用化学产业 '},
         {'value': '2', 'name': '化学生物学 '},
         {'value': '2', 'name': '化学工程与工艺 '},
         {'value': '2', 'name': '制药工程 '}
     ]},

    {'value': 22,
     'name': '历史文化学院',
     'children': [
         {'value': '10', 'name': '国际事务与国际关系'},
         {'value': '9 ', 'name': '档案学 '},
         {'value': '3 ', 'name': '历史学 '}
     ]},

    {'value': 29,
     'name': '外国语学院',
     'children': [
         {'value': '7', 'name': '英语'},
         {'value': '4', 'name': '英语+国际经济与贸易'},
         {'value': '5', 'name': '翻译'},
         {'value': '8', 'name': '法语'},
         {'value': '5', 'name': '日语'}
     ]},

    {'value': 34,
     'name': '教育学院',
     'children': [
         {'value': '20', 'name': '教育技术学'},
         {'value': '5 ', 'name': '教育学'},
         {'value': '9 ', 'name': '心理学'}
     ]},

    {'value': 20,
     'name': '文学院',
     'children': [
         {'value': '9', 'name': '汉语言文学'},
         {'value': '9', 'name': '编辑出版学'},
         {'value': '2', 'name': '汉语国际教育'}
     ]},

    {'value': 6,
     'name': '商学院',
     'children': [
         {'value': '3', 'name': '市场营销'},
         {'value': '2', 'name': '旅游管理'},
         {'value': '1', 'name': '人力资源管理'}
     ]},
]

treemap = (
    TreeMap()
        .add('各专业体育检测抽样人数', data,
             pos_left='center',  # 主图的位置
             tooltip_opts=opts.TooltipOpts(is_show=True),
             # 子标签展示，大小，字体
             label_opts=opts.LabelOpts(is_show=True, font_size=14,
                                       font_family='serif', vertical_align='top')
             )
        .set_global_opts(title_opts=opts.TitleOpts(title='矩形树图\n'),  # 图左上角:标题
                         legend_opts=opts.LegendOpts(is_show=True),  # 图上面中间:图例
                         toolbox_opts=opts.ToolboxOpts(is_show=True), # 图右上角:工具箱
                         # tooltip_opts=opts.TooltipOpts(is_show=True),  # 图上:提示框
                         # visualmap_opts=opts.VisualMapOpts(is_show=True),  # 图右下角:视觉映射
                         )
)

# 图的宽高
treemap.width='1000px'
treemap.height='600px'
#  保存为html文件
treemap.render('./data/treemap.html')
