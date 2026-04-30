# 使用request进行网络请求实现下载图片
import requests

def downlaod_pic(url):
    print(f'开始下载图片{url}.....')
    response=requests.get(url)
    print(f'图片{url}下载完成')
    print(
        response.status_code,
        response.headers,
    )

    # 保存到本地
    print(f'保存图片{url}.....')
    with open(url[-12:],'wb') as file:
        file.write(response.content)

def main():
    urls=[
        'https://www.bing.com/images/search?view=detailV2&ccid=U6tFOsCm&id=BB223B26568F53A5C98805C8BE6DBB143D3D6709&thid=OIP.U6tFOsCm23NIQTvQAkjR_gHaEP&mediaurl=https%3A%2F%2Fgd-hbimg.huaban.com%2Faff9f642ba8a7a981a16e6ddc0520d375e1e558aff846-TbvcZg_fw658&exph=377&expw=658&q=%E5%9C%B0%E5%9B%BE%E5%A4%A7%E5%B1%8F%E8%AE%BE%E8%AE%A1&FORM=IRPRST&ck=DDF3F2B280B3E7821070C11CBA0491AA&selectedIndex=1&itb=0&cw=1145&ch=578&ajaxhist=0&ajaxserp=0',
        'https://www.bing.com/images/search?view=detailV2&ccid=8Uqb1iCM&id=DBD27E80866198ADB062F4D450210E98E8A888F3&thid=OIP.8Uqb1iCMr93dYnJCBzS-KQHaEK&mediaurl=https%3A%2F%2Fgd-hbimg.huaban.com%2Ff077fa58198462612aa1a5f6297bc4c24c1c49ad11116a-c9y9eG_fw658&exph=370&expw=658&q=%E5%9C%B0%E5%9B%BE%E5%A4%A7%E5%B1%8F%E8%AE%BE%E8%AE%A1&form=IRPRST&ck=5D06E3DD6759D6E2FC27504261A962B3&selectedindex=2&itb=0&cw=1145&ch=578&ajaxhist=0&ajaxserp=0&vt=0&sim=11',
        'https://www.bing.com/images/search?view=detailV2&ccid=PQD8eNV0&id=6BE4E3E33F6535CCFB7B3720BA166DE0C7DF61AF&thid=OIP.PQD8eNV0BUlZlH2tTy4lOAHaEK&mediaurl=https%3A%2F%2Fi-blog.csdnimg.cn%2Fblog_migrate%2F83fe3abcac752adea8d63670826977fa.jpeg&exph=2160&expw=3840&q=%E5%9C%B0%E5%9B%BE%E5%A4%A7%E5%B1%8F%E8%AE%BE%E8%AE%A1&form=IRPRST&ck=C4C3D656C93649C3274D46DEC4098CAA&selectedindex=3&itb=0&cw=1145&ch=578&ajaxhist=0&ajaxserp=0&vt=0&sim=11'
    ]
    for url in urls:
        downlaod_pic(url)

main()
