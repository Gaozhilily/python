# !python3
# 电话号码和邮件.py -在剪贴板文本中查找电话号码和邮件
import pyperclip, re

#生成电话正则表达式
phoneregex=re.compile(r'''(
    (\d{4}|\(\d{4}\))? #区号
    (\s|-|\.)?         #分隔符
    (\d{8})            #后8位
    )''',re.VERBOSE)    

#生成电子邮件正则表达式
emailregex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+  #用户名
    @                  #@符号
    [a-zA-Z0-9.-]+     #域名
    (\.[a-zA-Z]{2,4})  #顶级域名
    )''',re.VERBOSE)

#查找剪贴板文本中电话号码和邮件
text=str(pyperclip.paste())
matches=[]
for groups in phoneregex.findall(text):
    phonenum='-'.join([groups[1],groups[3]])
    matches.append(phonenum)
for groups in emailregex.findall(text):
    matches.append(groups[0])
    
#将查找结果粘贴剪贴板
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('复制至剪贴板:')
    print('\n'.join(matches))
else:
    print('未找到电话号码或电子邮件地址.')

