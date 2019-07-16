# coding:utf-8  
print("hello world!")

def fun_ren(n):
    if n == 1:
        return 1
    else:
        return n * fun_ren(n-1)
    
print(fun_ren(5))