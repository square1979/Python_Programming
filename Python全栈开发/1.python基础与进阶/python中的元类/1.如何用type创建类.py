# 传统⽅式创建类(直观)
"""
class Foo(object):
v1 = 123

 def func(self):
 return 666
print(Foo)
"""
# ⾮传统⽅式（⼀⾏）
# 1 创建类型
# - 类名
# - 继承类
# - 成员
Fa = type("Foo", (object,), {"v1": 123, "func": lambda self: 666})
# 2 根据类创建对象
obj = Fa()
# 3 调⽤对象中的v1变量
print(obj.v1)
# 4 执⾏对象中的func⽅法
result = obj.func()
