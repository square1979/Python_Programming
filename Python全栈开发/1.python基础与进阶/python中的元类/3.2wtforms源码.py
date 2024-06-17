from wtforms.form import BaseForm
from wtforms.fields import simple


class FormMeta(type):
    def __init__(cls, name, bases, attrs):
        type.__init__(cls, name, bases, attrs)
        cls._wtforms_meta = None
        cls._unbound_fields = None
        cls._Wtforms_meta = None

    def __call__(cls, *args, **kwargs):
        if cls._unbound_fields is None:
            fields = []
            for name in dir(cls):
                if not name.startswith('_'):
                    unbound_field = getattr(cls, name)
                    if hasattr(unbound_field, '_formfield'):
                        fields.append((name, unbound_field))
            fields.sort(key=lambda x: (x[1].creation_counter, x[0]))
            cls._unbound_fields = fields
            # We keep the name as the second element of the sort to ensure a stable sort.
        # Create a subclass of the 'class Meta' using all the ancestors .
        if cls._wtforms_meta is None:
            bases = []
            for mro_class in cls.__mro__:
                if 'Meta' in mro_class.__dict__:
                    bases.append(mro_class.Meta)
                cls._wtforms_meta = type('Meta', tuple(bases), {})
                # 初始化时传递 fields 参数
        kwargs['fields'] = cls._unbound_fields
        return super(FormMeta, cls).__call__(*args, **kwargs)


def with_metaclass(meta, base=object):
    # FormMeta("NewBase". (BaseForm,), {} )
    # type( "NewBase", ( BaseForm,), {} )
    return meta("NewBase", (base,), {})


class NewBase(BaseForm, metaclass=FormMeta):
    pass


"""
class Form(NewBase):
    pass

"""


class Form(with_metaclass(FormMeta, BaseForm)):
    pass


# LoginForm其实是由FormMeta 创建的。
# 1.创建类时，会执⾏FormMeta 的__new__ 和__init__，内部在类中添加了两个类变量 _unbound_fields 和_wtforms_meta
class LoginForm(Form):
    name = simple.StringField(label='⽤户名', render_kw={'class': 'form-control'})
    pwd = simple.PasswordField(label='密码', render_kw={'class': 'form-control'})


form1 = LoginForm()
print(form1.name)  # 类变量
print(form1.pwd)  # 类变量

# 问题1:此时LoginForm是由 type or FormMeta创建?
"""
类中metaclass,⾃⼰类 由于metaclass定义的类来创建。
类继承某个类，⽗类metaclass, ⾃⼰类由于metaclass定义的类来创建。
"""
