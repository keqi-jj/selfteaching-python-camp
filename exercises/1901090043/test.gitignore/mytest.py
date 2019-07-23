def sort_func_decorator(func):
    def sort_num_func(*args,**kargs):
        func(*args,**kargs)
        sort_num(*args,**kargs)
    return sort_num_func
    
def sort_num(a,issort = False):
            if issort == True:
                b = sorted(a)
                print(b)
            else:
                return None

@sort_func_decorator
def get_num(a,issort = False):
     print(a)

a_nums = [1,5,3,9,0,4]
get_num(a_nums,issort=True)