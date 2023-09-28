#!/usr/bin/python3

#第一个注释
#print ("Hello, Python!")  #第二个注释
import math

'''
第三个注释
第四个注释
'''

'''

if True:
    print ("True")
else:
    print ("False")



if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    print ("False")


total = 1 + \
        2 + \
        3 + \
        4

name = ["I", 
        "am", 
        "Leon"]

print(name)

word = '字符串'
sentence = "这是一个句子"
paragraph = """这是一个段落，
可以由多行组成"""
'''
'''
str='123456789'

print (str)                            #输出字符串
print (str[0:-1])                      #输出第一个到倒数第二个的所有字符
print (str [0])                        #输出字符串第一个字符
print (str[2:5])                       #输出从第三个到开始到第六个的字符 （不包含）
print (str[2:])                        #输出从第三个开始后的所有字符
print (str[1:5:2])                     #输出第二个开始到第五个且每隔一个的字符 （步长为2）
print (str * 2)                        #输出字符串两次
print (str + '你好')                    #连接字符串

print ('--------------------------------------')

print ('hellow\nrunoob')                #使用反斜杠（\）+n 转义特殊字符
print (r'hellow\nrunoob')               #在字符串前面添加一个r， 表示原始字符， 不会发生转义
'''
'''
input("\n\n按下enter键后退出。")

import sys ; x = 'runoob' ; sys.stdout.write(x+'\n')
'''


'''
quotent = 17//3
reminder = 17%3
print ("##################################\n")
print (str(quotent) + "..." + str(reminder))
print ("\n##################################")
'''

'''
print (2**10)
'''

print (abs(-89))
print (math.ceil(4.1))
print (math.exp(8))
print (math.fabs(11.3))
print (math.floor(5.6))
print (math.log(100, 10))
print (math.log10(100))
print (max(56, 8545, 4545, 545, 48, 564648 ,5468, 524))
print (min(56, 8545, 4545, 545, 48, 564648 ,5468, 524))
print (math.modf(3.1415926))
print (math.pow(9, 11))
print (round(3.1415926, 3))
print (math.sqrt(4096))