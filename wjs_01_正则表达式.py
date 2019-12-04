import re

# re.match（正则表达式，需要处理的字符串）
ret = re.match(r"hello", "hello world")
# 连续数据用-(单个字符)
ret2 = re.match(r"超人[1-9]", "超人3")
# 中括号中加字母(单个字符)
ret3 = re.match(r"超人[1-9a-zA-Z]", "超人3A")
# 支持中文(单个字符)
ret4 = re.match(r"超人\w", "超人3A")
# .支持很很广理解为*但除了\n (单个字符)
ret5 = re.match(r"超人.", "超人3A")
# {}约束前一个\d的位数(单个字符)
ret6 = re.match(r"超人\d{1,2}", "超人34")
# ？约束前一个值可有可无(单个字符)
ret7 = re.match(r"\d{3,4}-?\d{8}", "021-12345678")


print(ret.group())
print(ret2.group())
print(ret3.group())
print(ret4.group())
print(ret5.group())
print(ret6.group())
print(ret7.group())