# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 22:46:20 2019

@author: Lily
"""
#定义collatz序列函数，参数number是偶数，则打印number/2，是奇数，则打印number*3+1
def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    elif number%2==1:
        print(number*3+1)
        return number*3+1
    
#输入任意正整数，并不断调用collatz函数，直至最终结果均为1
try:
    print('请输入一个正整数：')
    number = int(input())
    while number!=1:
        number=collatz(number)
except ValueError:
    print('输入错误，请输入一个正整数！')    

