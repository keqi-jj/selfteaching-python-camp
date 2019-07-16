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
    word_txt = re.findall(pattern,text)
    return dict(Counter(word_txt).most_common(count))

#参数：字符串文本，输出按汉子的统计排名
def stats_text_cn(text,count):
    pattern1 = re.compile( "[\u4E00-\u9FA5]+")
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 27') 
    #找到所有中文汉字
    words_txt = re.findall(pattern1,text)
    new_txt = ''
    for items in words_txt:
        new_txt = new_txt + items
    #用结巴函数进行分词，得到列表
    new_txt = list(jieba.cut(new_txt))
    new_txt1 = []
    #删除为一个字的词
    for items in new_txt:
        if len(items) > 1:
            new_txt1.append(items)     
    return dict(Counter(new_txt1).most_common(count))

#调用stats_text_en()，stats_text_cn()两个函数并且合并排序输出
def stats_text(text,count):   
    path = abspath('stats_word.py')
    if type(text) != str:
        raise ValueError('异常！你输入的不是字符串！',path+' line 46') 
    eng_txt = stats_text_en(text,count)
    chi_txt = stats_text_cn(text,count)
    #合并eng_txt，chi_txt
    merge_txt = dict(eng_txt,**chi_txt)
    return dict(Counter(merge_txt).most_common(count))
    
    

