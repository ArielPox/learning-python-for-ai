# 1.自定义异常类 表示更具体的异常信息，规则是：自定义异常类继承Exception 并且类的后缀是Error结尾
class MyError(Exception):
    def __init__(self,msg):
        super().__init__('异常1'+msg)

    def check_name(name):
        if len(name)>10:
            raise MyError('名字长度不能超过10个字符')
        else:
            print('名字长度正常')

    try:
        name=input('请输入名字：')
        check_name(name)
    except MyError as e:
        print(e)