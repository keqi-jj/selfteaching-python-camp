# coding:utf-8  
num_array = [0,1,2,3,4,5,6,7,8,9]
sor_array = sorted(num_array,reverse = True)
for i in sor_array:
   sor_array[9-i] = str(i)
num_txt = ''.join(sor_array)
#切片
num_txt = num_txt[2:8]
num_txt = sorted(num_txt)
#转整形
for i in num_txt:
    num_txt[int(i) - 2] = int(i)
#转2进制
for i in range(0,6):
    num_txt[i] = bin(num_txt[i])
print("*"*30 + "转2进制" + "*"*30)
print(num_txt)
#转8进制
for i in range(0,6):
    num_txt[i] = oct(int(num_txt[i],2))
print("*"*30 + "转8进制" + "*"*30)
print(num_txt)
#转16进制
for i in range(0,6):
    num_txt[i] = hex(int(num_txt[i],8))
print("*"*30 + "转16进制" + "*"*30)
print(num_txt)