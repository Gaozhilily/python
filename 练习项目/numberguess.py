# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 22:25:59 2019

@author: Lily
"""
#这是一个猜数字游戏
import random
secret_number=random.randint(1,20)
print('我想的是一个1-20间的数字.')

#让玩家做多猜6次
for guesstaken in range(1,7):
    print('猜一下我想的是几?')
    guess=int(input())
    if guess<secret_number:
        print('你猜小了.')
    elif guess>secret_number:
        print('你猜大了.')   
    else:
        break
if guess==secret_number:
    print('恭喜你，用'+str(guesstaken)+'次猜对了我的数字!')
else:
    print('太遗憾了，你没猜对.我想的数字是'+ str(secret_number) + '.')
        
