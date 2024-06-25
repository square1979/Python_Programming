# 要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducat'
print(motorcycles)

# 在列表末尾添加元素append
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducat')
print(motorcycles)

# 在列表中插⼊元素使⽤ insert() ⽅法可在列表的任意位置添加新元素
motorcycles.insert(0, 'ducat')
print(motorcycles)

# 从列表中删除元素知道要删除的元素在列表中的位置，可使⽤ del 语句
del motorcycles[0]
print(motorcycles)
# pop() ⽅法删除列表末尾的元素，并返回值可以赋值
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
# 删除列表中任意位置的元素也可以使⽤ pop()
print(motorcycles.pop(0))
# 根据值删除元素只知道要删除的元素的值，可使⽤ remove() ⽅法
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)

"""
练习 3.4：嘉宾名单 如果你可以邀请任何⼈⼀起共进晚餐，你会邀请哪些⼈？请创建⼀个列表，
其中包含⾄少三个你想邀请的⼈，使⽤这个列表打印消息，邀请这些⼈都来与你共进晚餐。
"""
list1 = ['旭旭宝宝', '一阵雨一阵奶', '大硕']
for i in list1:
    print(f"{i},邀请你共进晚餐！")

"""
练习 3.5：修改嘉宾名单 你刚得知有位嘉宾⽆法赴约，因此需要另外邀请⼀位嘉宾。
以完成练习 3.4 时编写的程序为基础，在程序末尾添加函数调⽤print()，指出哪位嘉宾⽆法赴约。
修改嘉宾名单，将⽆法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。再次打印⼀系列消息，向名单中的每位嘉宾发出邀请。
"""
print(f"{list1.pop(2)}无法参加晚宴\n")
list1.append('诸葛钢铁')
for i in list1:
    print(f"{i},邀请你共进晚餐！")

"""
练习 3.6：添加嘉宾 你刚找到了⼀张更⼤的餐桌，可容纳更多的嘉宾就座。请想想你还想邀请哪三位嘉宾。
以完成练习 3.4 或练习 3.5 时编写的程序为基础，在程序末尾添加函数
调⽤ print()，指出你找到了⼀张更⼤的餐桌。
使⽤ insert() 将⼀位新嘉宾添加到名单开头。
使⽤ insert() 将另⼀位新嘉宾添加到名单中间。
使⽤ append() 将最后⼀位新嘉宾添加到名单末尾。
打印⼀系列消息，向名单中的每位嘉宾发出邀请。
"""
print("我找到了⼀张更⼤的餐桌")
list1.insert(0, '韩茜茜')
list1.insert(2, '周杰伦')
list1.append('张杰')
for i in list1:
    print(f"{i},邀请你共进晚餐！")
print(list1)
"""
练习 3.7：缩短名单 你刚得知新购买的餐桌⽆法及时送达，因此只能邀请两位嘉宾。
以完成练习 3.6 时编写的程序为基础，在程序末尾添加⼀⾏代码，打印⼀条你只能邀请两位嘉宾共进晚餐的消息。
使⽤ pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为⽌。每次从名单中弹出⼀位嘉宾时，
都打印⼀条消息，让该嘉宾知道你很抱歉，⽆法邀请他来共进晚餐。余下两位嘉宾都打印⼀条消息，
指出他依然在受邀之列。
使⽤ del 将最后两位嘉宾从名单中删除，让名单变成空的。打印
该名单，核实名单在程序结束时确实是空的。
"""
print("抱歉，只能邀请两位嘉宾共进晚餐")
for i in range(0, len(list1)):
    if i >= 2:
        name = list1.pop()
        print(f"{name}⽆法邀请他来共进晚餐")
    else:
        print("您依然在受邀之列")
        del list1[0]

print(list1)
