# coding:utf-8  
import operator
import pprint
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
pattern = re.compile('[A-Z]*[a-z]+')
filt_txt = re.findall(pattern,text)
words_cnt = {}
for word in filt_txt:
    #word = word.strip()
    if not word in words_cnt:
        if word != "\n":
            words_cnt[word] = 1
    else:
        words_cnt[word] = words_cnt[word] + 1
sort_words_cnt = sorted(words_cnt.items(),key = lambda x:x[1],reverse = True)
pprint.pprint(sort_words_cnt)