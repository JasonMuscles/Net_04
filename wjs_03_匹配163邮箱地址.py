import re


def main():
    user_emails = input("请输入你的邮箱地址：")
    # 如果在正则表达式中需要用到某些特殊字符，如：？.! 时需要在他们前面添加一个反斜杠进行转义

    ret = re.match(r"[a-zA-Z_0-9]{4,20}@163\.com$", user_emails)
    if ret:
        print("%s邮箱输入格式正确" % user_emails)
    else:
        print("%s邮箱输入不符合规则。" % user_emails)


if __name__ == '__main__':
    main()
