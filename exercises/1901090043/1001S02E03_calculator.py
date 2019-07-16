# coding:utf-8  
def calculator():
        num_first = input("输入一个数：")
        num_first = num_first.strip()
        num_first = float(num_first)
        oper = input("输入运算符：")
        oper = oper.strip()
        num_second = input("输入另外一个数：")
        num_second = num_second.strip()
        num_second = float(num_second)

        if oper == '+':
                num_result = num_first + num_second
                print("结果是：",num_result)

        elif oper == "-":
                num_result = num_first - num_second
                print("结果是：",num_result)

        elif oper == "*":
                num_result = num_first * num_second
                print("结果是：",num_result)

        elif oper == "/":
                num_result = num_first / num_second
                print("结果是：",num_result)
        
        else:
                print("输入有误！")
calculator()
