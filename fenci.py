# -*- coding:utf-8 -*-

import jieba.analyse
import jieba.posseg as pseg
import xlrd

# s="投诉内容:用户发送818至10086查询活动优惠，查不到，因该服务已关闭，已解释情况，用户不接受，也不接受人工来电查询或APP或移动公众号查询，纠缠，要求我司解答何时复通此查询服务，请跟进，谢谢！营销案名称:短信渠道无法查询是否目标客户:否办理时间:2018-06-30 19:54:05办理渠道:短信无法办理反馈/提示内容:不相关客户标签类型:A类升级投诉客户，客服投诉类型：投诉申告->基础业务->基础营销->预存充值营销→无法参加营销活动，客户名称：蒙**，投诉用户联系电话：13790013831，投诉号码：13790013831，用户类型：3星客户（动感地带），用户归属地：佛山，故障时间：2018-07-01 09:24:21，受理员工号：FS13797(陈少红)，建单人部门：佛山→客服(佛山)中心→VIP热线室(佛山中心)→VIP室08组，建单人联系电话：，联系人：先生，联系地址：，最终回复时限：2018-07-01 14:12:21"
# seg_list=jieba.cut(s,cut_all=True)
# print(seg_list)
# print("Full Mode: " + "/ ".join(seg_list))
#
# seg_list = jieba.cut(s)
# print("Default Mode: " + "/ ".join(seg_list))
#
# a=jieba.analyse.extract_tags(s, topK=20, withWeight=False, allowPOS=())
# print("/".join(a))
#
# words = pseg.cut("我爱北京天安门")
# for word, flag in words:
#     print('%s %s' % (word, flag))
#
# words = pseg.cut(s)
# for word, flag in words:

#不限业务大类
def read_excel(file_path):
    excel_file = xlrd.open_workbook(file_path)
   # print(excel_file.sheet_names())
    o_topics = []
    for sheet in excel_file.sheets():
        if str(sheet.name).__contains__('事件单'):
            for i in range(1, sheet.nrows):
                o_topic = str(sheet.cell(i, 3).value)#只要工单描述的内容
                o_topics.append(o_topic)
            break
    return o_topics

def read_excel_top(file_path,top):
    excel_file = xlrd.open_workbook(file_path)
   # print(excel_file.sheet_names())
    o_topics = []
    for sheet in excel_file.sheets():
        if str(sheet.name).__contains__('事件单'):
            for i in range(1, sheet.nrows):
                if str(sheet.cell(i, 6).value) == top:
                    o_topic = str(sheet.cell(i, 3).value)#只要工单描述的内容
                    o_topics.append(o_topic)
            break
    return o_topics

#不限业务大类的
def hot_word_count(file_path,word_count):
    # word_count = {}
    o_topics = read_excel(file_path)
    for o_topic in o_topics:
        for word, flag in pseg.cut(o_topic):
            if flag=='nz':
                if not word_count.__contains__(word):
                    word_count[word] = 1
                else:
                    word_count[word] = word_count[word] + 1
    word_count_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    # for s in word_count_sorted:
    #     print(s)
    return word_count_sorted


# 限制了业务大类的return: {word: count, word: count}
def hot_word_count_top(file_path,word_count,top):
    # word_count = {}
    o_topics = read_excel_top(file_path,top)
    for o_topic in o_topics:
        for word, flag in pseg.cut(o_topic):
            if flag == 'nz':#自定义词
                if not word_count.__contains__(word):
                    word_count[word] = 1
                else:
                    word_count[word] = word_count[word] + 1
    word_count_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return word_count_sorted


def fenci(top,num,keyword,value):
    jieba.load_userdict(r'word/移动自定义词.txt')
    tichu = open('word/剔除的词.txt', 'r', encoding='utf8').read()
    ds_list=['佛山','广州','江门','茂名','清远','韶关','阳江','云浮','湛江','肇庆','中山','珠海']
    print(top)
    word_count = {}
    word_count_sorted={}
    for i in range(0,len(ds_list)):
        #print(ds_list[i])#地市名
        f=r'data/业务支撑集中化工单分析2018年7月/'+str(ds_list[i])+'.xlsx'
        #word_count_sorted=hot_word_count(f,word_count)
        word_count_sorted = hot_word_count_top(f, word_count,top) #根据业务大类来分词

    #f.write(top + '\n')
    #print(word_count_sorted)
    i=0
    for turble in word_count_sorted:
        if i < num :
            i=i+1
            if str(tichu).find(str(turble[0])) == -1:#不存在剔除的词里面
                keyword.append(str(turble[0]))
                value.append(turble[1])
                print(str(turble[0])+'|'+str(turble[1])+'\n')
                #f.write(str(turble[0])+'|'+str(turble[1])+'\n')
    return 0