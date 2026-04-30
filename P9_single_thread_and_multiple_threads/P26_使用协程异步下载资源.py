import aiohttp
import asyncio

async def downlaod_pic(session,url):
    print(f'开始下载图片{url}.....')
    # 发送网络请求 获取到图片之后就等待服务器把数据返回 等待的时间就是IO等待时间
    response=await session.get(url)
    # 等待数据-图片数据可能会分多次传输 需要等待数据全部读完 等待的时间也是IO等待
    content=await response.read()
    with open(url[-12:],'wb') as file:
        file.write(content)
        print(f'图片{url[-8:]}保存完毕')
    # 释放连接资源 告诉aiohttp回收
    await response.release()
async def main():
    urls=[
        'https://www.bing.com/images/search?view=detailV2&ccid=8Uqb1iCM&id=DBD27E80866198ADB062F4D450210E98E8A888F3&thid=OIP.8Uqb1iCMr93dYnJCBzS-KQHaEK&mediaurl=https%3A%2F%2Fgd-hbimg.huaban.com%2Ff077fa58198462612aa1a5f6297bc4c24c1c49ad11116a-c9y9eG_fw658&exph=370&expw=658&q=%E5%9C%B0%E5%9B%BE%E5%A4%A7%E5%B1%8F%E8%AE%BE%E8%AE%A1&form=IRPRST&ck=5D06E3DD6759D6E2FC27504261A962B3&selectedindex=2&itb=0&cw=1145&ch=578&ajaxhist=0&ajaxserp=0&vt=0&sim=11',
        'https://www.bing.com/images/search?view=detailV2&ccid=PQD8eNV0&id=6BE4E3E33F6535CCFB7B3720BA166DE0C7DF61AF&thid=OIP.PQD8eNV0BUlZlH2tTy4lOAHaEK&mediaurl=https%3A%2F%2Fi-blog.csdnimg.cn%2Fblog_migrate%2F83fe3abcac752adea8d63670826977fa.jpeg&exph=2160&expw=3840&q=%E5%9C%B0%E5%9B%BE%E5%A4%A7%E5%B1%8F%E8%AE%BE%E8%AE%A1&form=IRPRST&ck=C4C3D656C93649C3274D46DEC4098CAA&selectedindex=3&itb=0&cw=1145&ch=578&ajaxhist=0&ajaxserp=0&vt=0&sim=11'
    ]
    # 创建会话的对-发送请求单工具
    session=aiohttp.ClientSession()
    # 创建多个的协程对象交给事件循环执行
    contine_list=[downlaod_pic(session,url) for url in urls]
    # 将多个协程对象交给事件循环执行
    await asyncio.gather(*contine_list)
    # 关闭会话
    await session.close()

# 开启事件循环
asyncio.run(main())

