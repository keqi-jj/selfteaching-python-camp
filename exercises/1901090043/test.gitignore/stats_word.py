import re

#字符串文本按照单词排序
def stats_text_en(text):
    pattern = re.compile( "[A-Z]*[a-z]+")
    filt_txt = re.findall(pattern,text)
    word_cnt = {}
    for item in filt_txt:
        if item not in word_cnt:
            word_cnt[item] = 1
        else:
            word_cnt[item] += 1
    word_cnt = sorted(word_cnt.items(),key = lambda x:x[1],reverse = True)
    return word_cnt

#参数：字符串文本，输出按汉子的统计排名
def stats_text_cn(text):
    pattern = re.compile( "[\u4E00-\u9FA5]")
    filt_txt = re.findall(pattern,text)
    word_cnt = {}
    for item in filt_txt:
        item = item.strip()
        if item not in word_cnt:
            word_cnt[item] = 1
        else:
            word_cnt[item] += 1        
    #降序排列
    word_cnt = sorted(word_cnt.items(),key = lambda x:x[1] ,reverse = True)
    return word_cnt

#调用stats_text_en()，stats_text_cn()两个函数并且合并排序输出
def stats_text(text):
    eng_txt = dict(stats_text_en(text))
    chi_txt = dict(stats_text_cn(text))
    #合并dic，dic1
    merge_txt = dict(eng_txt,**chi_txt)
    #对新字典排序统计
    merge_txt = sorted(merge_txt.items(),key = lambda x:x[1],reverse = True)
    return merge_txt
