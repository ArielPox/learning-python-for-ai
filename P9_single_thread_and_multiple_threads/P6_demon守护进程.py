# 方式	     主线程退出后	        是否执行finally	            适用场景
# 普通线程	  等待跑完	                是	            业务逻辑、文件写入
# 守护线程    daemon=True直接杀死	    否	            后台心跳、监控、辅助任务
# terminate()	立即杀死	                否	                几乎不推荐用

import threading
import time

def work(msg):
    try:
        print(f'{msg}子线程开始工作...')
        while True:
            print(f'{msg}子线程工作中...')
            time.sleep(0.5)
    finally:
        print('finally 资源清理 收尾 子线程结束')

if __name__ == '__main__':
    print('主线程开始')
    # 创建守护进程
    t = threading.Thread(target=work,daemon=True,args=('守护子线程',))
    t.start()
    # t1=threading.Thread(target=work,args=('普通子线程',))
    # t1.start()
    print('主进程跑3秒结束')
    time.sleep(3)
    print('主线程结束')