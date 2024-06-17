from wtforms import Form
from wtforms.fields import simple


class LoginForm(Form):
    name = simple.StringField(label='⽤户名',
                              render_kw={'class': 'form-control'})
    pwd = simple.PasswordField(label='密码', render_kw={'class': 'form-control'})


form = LoginForm()
print(form.name)  # 类变量
print(form.pwd)  # 类变量
