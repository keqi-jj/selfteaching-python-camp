# coding:utf-8  
import re

text = '''
The Zen of Python, by Tim Peters Beautiful is better than ugly.
Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.
Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.
Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
 '''
re_text = text.replace('better','worse',text.count('better'))
print('把better转化为worse'.center(150,'*'))
print("替换字符结果为：",re_text)
print('删除含有ea的单词'.center(150,'*'))

pattern = re.compile('[A-Z]*[a-z]+')
filt_txt = re.findall(pattern,text)
del_text = []
for item in filt_txt:
    if not "ea" in item:
        del_text.append(item)
print(del_text)

print('把单词大小写进行翻转'.center(150,'*'))
swi_txt = []
for item in range(0,len(del_text)):
    swi_txt.append(del_text[item].swapcase())
print(swi_txt)

print('单词字母升序'.center(150,'*'))
sor_word = sorted(swi_txt,key = str.lower)
print(sor_word)




    