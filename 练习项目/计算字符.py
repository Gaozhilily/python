#计算字符串中每个字符出现的次数
import pprint
def countm():
    messages=input()
    count={}
    for character in messages:
        count.setdefault(character,0)
        count[character]=count[character]+1
    pprint.pprint(count)
    
    