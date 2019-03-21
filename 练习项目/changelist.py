# -*- coding: utf-8 -*-

#编写一个程序，将输入的列表值，输出为字符串，该字符串包含所有表项
#表项之间以逗号和空格分隔，并在最后一个表项之前插入and
spam = ['apples', 'bananas', 'tofu', 'cats']
def change(list):
    length=len(list)
    s=''
    if length==0:
        return('该列表为空')
    elif length==1:
        return str(list[0])
    else:
        for i in range(length-2):
            s=s+str(list[i])+', '
        s=s+str(list[i])+' and '+str(list[-1])
        return s
s=change(spam)
print(s)