# 修改字符串的⼤⼩写
message = "nEw woRld"
print(message.title())
print(message.upper())
print(message.lower())

# 在字符串中使⽤变量
message1 = "new world"
print(f"信息内容为：{message1}")

# 使⽤制表符或换⾏符来添加空⽩ - 字符串中添加制表符，可使⽤字符组合 \t：
message2 = "newworld"
print("\tmessage2 ")
# 使⽤制表符或换⾏符来添加空⽩ - 字符串中添加换⾏符，可使⽤字符组合 \n：
message3 = "system"
print("\nmessage3 ")

# 字符串右端没有空⽩使⽤ rstrip()；左端的空⽩或同时删除字符串两端的空⽩，分别使⽤ lstrip()和 strip()
message4 = '  system   '
print(f"初始字符为：{message4}")
print(f"rstrip()处理：{message4.rstrip()}")
print(f"lstrip()处理：{message4.lstrip()}")
print(f"strip()处理：{message4.strip()}")

# 删除前缀使用removeprefix() ⽅法，括号内输⼊了要从字符串中删除的前缀。
print(f"removeprefix() ⽅法处理：{message4.removeprefix('  sys')}")

# 正确地使⽤单引号和双引号
message = "One of Python's strengths is its diverse community."
print(message)
# 原因是没有正确地使⽤引号将字符串引起来
# message = 'One of Python's strengths is its diverse community.'
# print(message)

"""
练习 2.3：个性化消息 ⽤变量表⽰⼀个⼈的名字，并向其显⽰⼀条消息。显⽰的消息应⾮常简单，如下所⽰。
Hello Eric, would you like to learn some Python today?
"""
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

"""
练习 2.4：调整名字的⼤⼩写 ⽤变量表⽰⼀个⼈的名字，再分别以全⼩写、全⼤写和⾸字⺟⼤写的⽅式显⽰这个⼈名。
"""
name = "jay chou"
print(name.lower())
print(name.upper())
print(name.title())

"""
练习 2.5：名⾔ 1 找到你钦佩的名⼈说的⼀句名⾔，将这个名⼈的姓名和名⾔打印出来。输出应类似于下⾯这样（包括引号）。
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
"""
print("Albert Einstein once said, “A person who never made a mistake never tried anything new.”")

"""
练习 2.6：名⾔ 2 重复练习 2.5，但⽤变量 famous_person 表⽰名⼈的姓名，
再创建要显⽰的消息并将其赋给变量 message，然后打印这条消息。
"""
famous_person = "Albert Einstein"
message = "“A person who never made a mistake never tried anything new.”"
print(f"{famous_person} once said, {message}")

"""
练习 2.7：删除⼈名中的空⽩ ⽤变量表⽰⼀个⼈的名字，并在其开头和末尾都包含⼀些空⽩字符。
务必⾄少使⽤字符组合 "\t" 和 "\n" 各⼀次。打印这个⼈名，显⽰其开头和末尾的空⽩。
然后，分别使⽤函数lstrip()、rstrip() 和 strip() 对⼈名进⾏处理，并将结果打印出来。
"""
name = "  巴旦木公主  "
print(name)
print(f"\t{name}")
print(f"\n{name}")
print(name.lstrip())
print(name.rstrip())
print(name.strip())

"""
练习 2.8：⽂件扩展名 Python 提供了 removesuffix() ⽅法，其⼯作原理与 removeprefix() 很像。
请将值 'python_notes.txt'赋给变量 filename，再使⽤ removesuffix() ⽅法来显⽰不包含扩展名的⽂件名
"""
filename = "python_notes.txt"
print(filename.removesuffix('.txt'))
