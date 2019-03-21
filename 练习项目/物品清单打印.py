#好玩游戏物品清单程序
#定义函数displaystuff，将清单中的物品打印输出
def displaystuff(inventory):
    print('Inventory:')
    item_total=0
    for k,v in inventory.items():
        print(str(v)+' '+ k)
        item_total+=v
    print('Total numbers of invertory is ' + str(item_total))
    
#定义增加物品函数，将新增物品清单保存并输出
#方法一
def addtoinventory(inventory,additems):
    for items in additems:
        if items in inventory.keys():
            inventory[items]+=1
        else:
            inventory[items]=1
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv=addtoinventory(inv,dragonLoot )
displaystuff(inv)

#方法二
def addtoinventory(inventory,additems):
    for items in additems:
        inventory.setdefault(items,0)
        inventory[items]+=1
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv=addtoinventory(inv,dragonLoot )
displaystuff(inv)