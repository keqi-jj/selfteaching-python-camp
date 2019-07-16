# coding:utf-8  
import mymodule.stats_word as stw

text = 'abddd,plo'
try:
    #对列表中中英文字符，进行统计降序排列
    sort_txt = stw.stats_text_en(text)
except ValueError as result:
    print(result)

print(sort_txt)