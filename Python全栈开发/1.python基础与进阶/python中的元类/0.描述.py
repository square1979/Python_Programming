"""
Python 中的元类是一种高级的编程技术，允许你在定义类时控制类的创建行为。
元类实际上是类的类，它们用于定义类的行为、结构和初始化过程。
以下是元类的一些主要功能和用途：
1.控制类的创建过程：
    元类允许你拦截类的创建过程，从而在类被实际创建之前或之后执行自定义的逻辑。
    这包括定义类的属性、方法、类级别的验证和初始化等。
2.实现单例模式：
    使用元类可以实现单例模式，确保一个类只能有一个实例。
3.验证和修改类的属性和方法：
    元类可以检查和修改类的属性和方法。这对于强制实施编码标准、添加额外的行为或自动化任务非常有用。
4.注册和插件系统：
    元类可用于创建注册表和插件系统，使得其他类能够自动注册到特定的管理系统中
5.动态创建类：
    元类使得你可以在运行时动态创建类，这对于某些框架和库（如 ORM）特别有用。
"""


# 定义一个元类
class ControlMeta(type):
    def __new__(cls, name, bases, attrs):
        # 在创建类之前，可以检查和修改类的属性和方法
        print(f"Creating class: {name}")
        print(f"Bases: {bases}")
        print(f"Attributes:")
        for key, value in attrs.items():
            print(f"  {key}: {value}")

        # 修改类的属性示例：给类添加一个新方法
        def new_method(self):
            print(f"Hello from {name} instance!")

        attrs['new_method'] = new_method

        # 创建类对象
        new_cls = super().__new__(cls, name, bases, attrs)

        # 可以在创建类之后执行其他逻辑，如注册类或处理类的特定行为

        return new_cls


# 使用控制类创建的元类
class MyClass(metaclass=ControlMeta):
    class_attr = "Class Attribute"

    def __init__(self, data):
        self.data = data

    def instance_method(self):
        print(f"Instance method called with data: {self.data}")

    def new_method(self):
        pass


# 创建 MyClass 的实例
obj = MyClass("Hello World")

# 调用新添加的方法
obj.new_method()

# 调用实例方法
obj.instance_method()

"""
Expected Output:

Creating class: MyClass
Bases: ()
Attributes:
  __module__: __main__
  __qualname__: MyClass
  class_attr: Class Attribute
  __init__: <function MyClass.__init__ at 0x...>
  instance_method: <function MyClass.instance_method at 0x...>
Hello from MyClass instance!
Instance method called with data: Hello World
"""
