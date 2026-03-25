# 语法错误：代码写错，运行不了
# 异常：运行出错，可捕获处理
# 万能模板：try-except-else-finally
# 常用操作：捕获、抛出、自定义、传递
# 不管是不是发生异常 try catch之后的代码都会执行 直接写except 会直接捕捉到程序中所有的异常


# 1.捕捉指定的异常
# try:
#     a=int(input('请输入数字：'))
#     b=int(input('请输入数字：'))
#     result=a / b
#     print(f'a/b={result}')
# except ZeroDivisionError:
#     print('除数不能为0')
# except ValueError:
#     print('请输入数字')

# 2.验证异常类之间的关系
# print(issubclass(ZeroDivisionError,ArithmeticError))
# print(issubclass(ArithmeticError,Exception))
# print(issubclass(Exception,BaseException))
# print(issubclass(ValueError,Exception))
# print(issubclass(KeyboardInterrupt,Exception))
# print(issubclass(SystemExit,Exception))


# 3.捕获到异常的详细信息
# try:
#     a=int(input('请输入数字：'))
#     b=int(input('请输入数字：'))
#     print(x)
#     result=a / b
#     print(f'a/b={result}')
# except ZeroDivisionError:
#     print('除数不能为0')
# except ValueError:
#     print('请输入数字')
# except Exception as e:
#     print(f'异常信息{e}')
#     print(f'异常类型{type(e)}')
#     print(f'异常参数{e.args}')
#     print(f'异常文件名{e.__traceback__.tb_frame.f_code.co_filename}')

# 4.完整的处理规则
try:
    a=int(input('请输入数字：'))
    b=int(input('请输入数字：'))
    result=a / b
    print(f'a/b={result}')
except(ZeroDivisionError,ValueError,Exception) as e:
    if isinstance(e,ZeroDivisionError):
        print('除数不能为0')
    elif isinstance(e,ValueError):
        print('请输入数字')
    else:
        print(f'异常信息{e}')
        print(f'异常类型{type(e)}')
        print(f'异常参数{e.args}')
        print(f'异常文件名{e.__traceback__.tb_frame.f_code.co_filename}')
else:
    print('没有异常')
finally:
    print('无论是否异常都会执行')