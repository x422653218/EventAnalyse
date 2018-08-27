import fenci
import pandas as pd
from pyecharts import Bar, Page, WordCloud,Pie

def tochart(path):
    df = pd.read_excel(path,sheet_name=0,encoding='ANSI')
    df.reset_index()

    page = Page(page_title='7月事件单分析TOP10')
    #Bar
    bar = Bar(width=1000,height=700)
    collist=df.columns.values.tolist()
    fenlei=df[collist[0]]
    for col in range(1,len(collist)-1):
        ds=collist[col]
        list2=df[ds]
        bar.add(ds,fenlei,list2,is_stack=True, bar_category_gap='40%',xaxis_interval=0, xaxis_rotate=15, yaxis_rotate=30)
    page.add_chart(bar,name="bar")

    #词云图+饼图
    top=""
    num=30
    wordcloud=[]
    pie=[]
    for i in range(0, 3):
        keyword = []
        value = []
        top = fenlei[i]
        fenci.fenci(top,num,keyword,value)#调用fenci
        print(keyword,value)
        #词云图
        wordcloud.append(WordCloud(title='↑关键词分析(TOP30)：'+str(top),title_text_size=14, title_top='bottom',width=500, height=500))
        wordcloud[i].add(top,keyword,value,word_size_range=[20,60],shape='diamond')
        page.add_chart(wordcloud[i],name='wordcloud'+str(i))
        #饼图
        pie.append(Pie(title='↑关键词分析(TOP10)：' + str(top),title_text_size=14, title_top='bottom',width=600, height=500))
        pie[i].add(top, keyword[0:10], value[0:10],
                   radius=[30, 60],label_text_color=None,is_label_show=True,
                   legend_orient="vertical",legend_pos="left")
        page.add_chart(pie[i], name='pie'+str(i))
        print('-' * 10)

    page.render('7月事件单分析TOP10+关键词.html')
    return 0