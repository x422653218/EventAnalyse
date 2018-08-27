import pandas as pd
import numpy as np
from pyecharts import Bar

df = pd.read_excel('data/佛山小组TOP10汇总.xlsx',sheet_name=0,encoding='ANSI')
#做一个数据透视
m=pd.pivot_table(df,index=['业务大类'],values=['事件单量'],columns=['地市'],aggfunc=[np.sum],fill_value=0,margins=True)

# m.drop(m.index[[0,1]],inplace=True)
m.to_csv('data/huizong.csv',encoding='ANSI')
