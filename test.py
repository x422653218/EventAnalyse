# -*- coding:utf-8 -*-

# import pandas as pd
# import numpy as np
# from pyecharts import Page
#
# #pandas类型的数据处理
# index = pd.date_range('2/1/2017',periods = 6,freq = 'M')
# df1 = pd.DataFrame(np.random.randn(6),index = index)
# df2 = pd.DataFrame(np.random.randn(6),index = index)
# df1_value = [i[0] for i in df1.values]
# df2_value = [i[0] for i in df2.values]
# #print type(df1_value) 列表
#
#
# #元组列表
# d = [(11,19),(12,21),(13,32),(10,20),(10,20),(10,33)]
# dat = dict(d)
# d1 = dat.keys()
# d2 = dat.values()
# #print type(d1)  列表
#
# #列表数据
# attr = ['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
# v1 = [11,12,13,10,10,10]
# v2 = [19,21,32,20,20,33]
#
# from pyecharts import Bar
#
# page = Page()   #实例化，同一网页按顺序展示多图
# bar = Bar('bar示例图','ryana')
# bar.add('test',index,df1_value,mark_point = ['average'])
# bar.add('test',attr,v1,mark_line = ['max'])
# page.add(bar)
#
# from pyecharts import Line
#
# line = Line('折线图示例')
# #line.add('test',attr,v1,mark_point = 'average')
# line.add('test',attr,v2,is_fill = True,area_opacity = 0.3) #面积图
# page.add(line)
#
# from pyecharts import Pie
#
# pie = Pie('饼图示例')
# #pie.add('test',attr,v1,is_label_show = True)
# pie.add('test',attr,v2,radius = [40,75],is_label_show = True) #饼环图
# page.add(pie)
#
# """
# #组合图line+pie
# from pyecharts import Grid
#
# grid = Grid()
# grid.add(line, grid_right="10%")
# grid.add(pie, grid_left="10%")
# grid.render()
# """
#
# from pyecharts import Scatter
#
# scatter = Scatter('散点图示例')
# scatter.add('test',v1,v2)
# page.add(scatter)
#
# from pyecharts import HeatMap
# import random
#
# x_axis = ['1a','2a','3a','4a','5a','6a','7a','8a','9a']
# y_axis = ['Sat','Fri','Thu','Wed','Tue','Mon','Sun']
#
# dataH = [[i,j,random.randint(0,50)] for i in range(9) for j in range(7)]
# heatmap = HeatMap('热力图示例')
# heatmap.add('test',x_axis,y_axis,dataH,is_visualmap = True,visual_text_color = "#000",visual_orient='horizontal')
# page.add(heatmap)
#
# from pyecharts import Kline
#
# dataK = [[2320.26,2320.33,2287.4,3513.4],[2340.26,2310.33,2187.4,2513.4],[2329.26,2420.33,2257.4,2573.4],
# [2321.26,2370.33,2187.4,3013.4],[2380.26,2220.33,2487.4,3113.4],[2350.26,2520.33,2087.4,2813.4],
# [2300.26,2390.33,2187.4,2413.4]]
#
# kline = Kline('K线图示例')
# kline.add('test',['2017/8/{}'.format(i+1) for i in range(7)],dataK)
# page.add(kline)
#
#
# from pyecharts import WordCloud
#
# dataW = {'Python':55,'HBASE':49,'JAVA':72,'MongoDB':88,'SAS':39,'Spark':63}
#
# wordcloud = WordCloud('词云图例',width = 1200,height = 720)
# wordcloud.add('test',dataW.keys(),dataW.values(),word_size_range = [20,80])
# page.add(wordcloud)
#
# page.render(r'echart.html')

import jieba
import jieba.posseg as pseg

jieba.load_userdict(r'自定义词.txt')
jieba.suggest_freq(('请', '协助', '处理', '核查'),False)
s="请协助办理，投诉内容:用户发送818至10086查询活动优惠，查不到，因该服务已关闭，已解释情况，用户不接受，也不接受人工来电查询或APP或移动公众号查询，纠缠，要求我司解答何时复通此查询服务，请跟进，谢谢！营销案名称:短信渠道无法查询是否目标客户:否办理时间:2018-06-30 19:54:05办理渠道:短信无法办理反馈/提示内容:不相关客户标签类型:A类升级投诉客户，客服投诉类型：投诉申告->基础业务->基础营销->预存充值营销→无法参加营销活动，客户名称：蒙**，投诉用户联系电话：13790013831，投诉号码：13790013831，用户类型：3星客户（动感地带），用户归属地：佛山，故障时间：2018-07-01 09:24:21，受理员工号：FS13797(陈少红)，建单人部门：佛山→客服(佛山)中心→VIP热线室(佛山中心)→VIP室08组，建单人联系电话：，联系人：先生，联系地址：，最终回复时限：2018-07-01 14:12:21"

words = pseg.cut(s)
for word, flag in words:
    if flag=='n' or flag=='a' or flag=='v' or flag=='vd' or flag=='vn' or flag=='nz':
        print('%s %s' % (word, flag))