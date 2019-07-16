# coding:utf-8  
from os.path import *
from collections import Counter
import re

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
    pattern = re.compile( "[\u4E00-\u9FA5]")
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 27') 
    filt_txt = re.findall(pattern,text)
    return dict(Counter(filt_txt).most_common(count))

#调用stats_text_en()，stats_text_cn()两个函数并且合并排序输出
def stats_text(text,count):   
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 46') 
    eng_txt = stats_text_en(text)
    chi_txt = stats_text_cn(text)
    #合并dic，dic1
    merge_txt = dict(eng_txt,**chi_txt)
    #对新字典排序统计
    return Counter(merge_txt).most_common(count)
    
    

