class MyType(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        new_cls = super().__new__(cls, *args, **kwargs)
        return new_cls

    def __call__(self, *args, **kwargs):
        # 调⽤⾃⼰的那个类 __new__ ⽅法去创建对象
        empty_object = self.__new__(self)

        # 调⽤你⾃⼰的__init__ ⽅法取初始化
        self.__init__(empty_object, *args, **kwargs)
        return empty_object


# 假设Foo是一个对象，由MyType创建
# Foo类其实是一个MyType的对象
# Foo（） -> MyType对象（）
class Foo(object, metaclass=MyType):
    def __init__(self, name):
        self.name = name


v1 = Foo("alex")
print(v1)
print(v1.name)
