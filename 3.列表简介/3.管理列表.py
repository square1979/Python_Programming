name = ['direct', 'found', 'admin', 'bennie', 'check']
print(name)
# 1.使⽤ sort() ⽅法对列表进⾏永久排序
name.sort()
print(name)
# 2.向 sort() ⽅法传递参数 reverse=True 即可与字⺟顺序相反的顺序排列列表元素
name.sort(reverse=True)
print(name)
# 3.保留列表元素原来的排列顺序，并以特定的顺序呈现它们，可使⽤sorted() 函数。
num = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(num))
print(sorted(num, reverse=True))
print(num)
# 4.要反转列表元素的排列顺序，可使⽤ reverse() ⽅法
song = ['god is girl', 'hope', 'friends', 'prefect']
song.reverse()
print(song)
# 5.使⽤ len() 函数可快速获悉列表的⻓度
print(len(song))

# 6. 练习 3.8：放眼世界
place = ['tianjin', 'shanghai', 'chongqing', 'india', 'british']
# (1) 使⽤ sorted() 按字⺟顺序打印这个列表，不要修改它。
print(sorted(place))
print(place)
# (2) 使⽤ sorted() 按与字⺟顺序相反的顺序打印这个列表，不要修改它。
print(sorted(place, reverse=True))
print(place)
# (3) 使⽤ reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了
place.reverse()
print(place)
place.reverse()
print(place)
# (4) 使⽤ sort() 修改该列表，使其元素按字⺟顺序排列。打印该列表，核实排列顺序确实变了
place.sort()
print(place)
place.sort(reverse=True)
print(place)

# 7. 练习 3.9：晚餐嘉宾
print(f"共邀请了{len(place)}个人参加晚宴")
