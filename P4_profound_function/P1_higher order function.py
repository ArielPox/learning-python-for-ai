# 高阶函数：当一个函数的参数是一个函数，或者返回值是函数，那么这个函数就是高阶函数
# 可以把行为的独立出去，传入不同的函数实现不同的逻辑
def info(msg):
    return 'remind——'+msg

def warn(msg):
    return 'warning——'+msg
def error(msg):
    return 'error——'+msg

def log(func,text):
    print(func(text))

log(info,'提示')
log(warn,'警告')
log(error,'错误')
