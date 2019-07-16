#coding:utf-8
from os.path import *
from collections import Counter
import re
import jieba

#字符串文本按照单词排序
def stats_text_en(text,count):
    pattern = re.compile( "[A-Z]*[a-z]+")
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 9') 
    filt_txt = re.findall(pattern,text)
    return dict(Counter(filt_txt).most_common(count))

#参数：字符串文本，输出按汉子的统计排名
def stats_text_cn(text,count):
    pattern = re.compile( "[\u4E00-\u9FA5]+")
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 27') 
    #找到所有中文汉字
    filt_txt = re.findall(pattern,text)
    new_txt = ''
    for items in filt_txt:
        new_txt = new_txt + items
    #用结巴函数进行分词，得到列表
    sep_txt = list(jieba.cut(new_txt))
    sep_txt1 = []
    #删除为一个字的词
    for items in sep_txt:
        if len(items) > 1:
            sep_txt1.append(items)
    return dict(Counter(sep_txt1).most_common(count))

#调用stats_text_en()，stats_text_cn()两个函数并且合并排序输出
def stats_text(text,count):   
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 46') 
    eng_txt = stats_text_en(text,count)
    chi_txt = stats_text_cn(text,count)
    #合并dic，dic1
    merge_txt = dict(eng_txt,**chi_txt)  
    #对新字典排序统计
    result_txt = Counter(merge_txt).most_common(count)
    return result_txt
    
    

