class MyType(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        # 先判断是否已有对象，有则不创建 没有则创建
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)

        # 调用你自己的那个类 __init__ 去初始化
        cls.__init__(cls.instance, *args, **kwargs)
        return cls.instance


class Singleton(object, metaclass=MyType):
    pass


class Foo(Singleton):
    pass


v1 = Foo()
v2 = Foo()
print(v1)
print(v2)
