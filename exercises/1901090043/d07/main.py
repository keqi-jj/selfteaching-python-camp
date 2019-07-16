# coding:utf-8  
from os import path
import stats_word as stw

cwd = path.abspath(path.dirname(__file__))
txt_path = path.join(cwd,'text.txt')
#读取/007/text.txt
file_content = ''
with open(txt_path,'r') as file_obj:
    for line in file_obj:
        file_content = file_content + line
#对列表中中英文字符，进行统计降序排列
sort_txt = stw.stats_text(file_content)

print(sort_txt)