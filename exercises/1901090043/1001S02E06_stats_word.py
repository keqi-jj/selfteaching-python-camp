# coding:utf-8  
import pprint
import re

text = '''1. 在 1001S02E06_stats_word.py 中定义⼀一个名为 stats_text_cn 的函数，函数接受⼀一 个字符串串 text 作为参数
2. 实现该函数的功能:统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列列的 数组
3. 为 stats_text_cn 添加注释说明he Zen of Python, by Tim Peters Beautiful is better than ugly.
Explicit is better'''

#字符串文本按照单词排序
def stats_text_en(text):
    pattern = re.compile( "[A-Z]*[a-z]+")
    filt_txt = re.findall(pattern,text)
    words_cnt = {}
    for item in filt_txt:
        if item not in words_cnt:
            words_cnt[item] = 1
        else:
            words_cnt[item] += 1
    words_cnt = sorted(words_cnt.items(),key = lambda x:x[1],reverse = True)
    return words_cnt

#参数：字符串文本，输出按汉子的统计排名
def stats_text_cn(text):
    pattern1 = re.compile( "[\u4E00-\u9FA5]")
    filt_txt = re.findall(pattern1,text)
    chi_words_txt = {}
    for item in filt_txt:
        item = item.strip()
        if item not in chi_words_txt:
            chi_words_txt[item] = 1
        else:
            chi_words_txt[item] += 1        
    #把汉子装入词典
    chi_words_txt = sorted(chi_words_txt.items(),key = lambda x:x[1] ,reverse = True)
    return chi_words_txt

pprint.pprint(stats_text_en(text))