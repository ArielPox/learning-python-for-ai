 # with是python里面用来自动关闭资源的语法 比如文件 锁以及数据库
 # 上下文管理协议
 # __enter__()和__exit__()方法
 # with语句会自动调用__enter__()方法，并把__exit__()方法的返回值作为with语句的返回值
 # 是要一个类里面实现了enter以及exit的魔法方法，进入with时候自动调用的enter里面方法，退出with时候自动调exit里面方法

class Myfile:
     def __init__(self,filename,mode):
         self.filename=filename
         self.mode=mode
         self.file=None
     def __enter__(self):
         self.file=open(self.filename,self.mode)
         # 返回文件对象之后会复赋值给 with语句中as之后的变量
         print('entry')
         return self.file
     def __exit__(self, exc_type, exc_val, exc_tb):
         print('exit')
         #当exit的代码发生异常时候 exit方法的返回值为True的时候 with语句会自动将异常抛给调用者，否则with语句会忽略异常
         if exc_type:
             print('异常类型：',exc_type)
             print('异常值：',exc_val)
             print('异常追踪：',exc_tb)
         if self.file and not self.file.closed:
             self.file.close()

with Myfile('test1.txt','w') as f:
    f.write('hello world')
    # f.sound()