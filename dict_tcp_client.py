'''
dict 客户端
功能:根据用户输入，发送请求，得到结果
结构
一级界面：————》注册————》登录————》 退出

二级界面：————》查单词 历史记录 注销

'''
from socket import *
from getpass import getpass  # 运行终端

# 服务器地址
ADDR = '127.0.0.1,8000'


# 搭建客户端网络
def main():
    s = socket()
    s.connect(ADDR)
    while True:
        print("""
        ++++++++++Welcome++++++++++
        1.注册    2.登录    3退出
        +++++++++++++++++++++++++++
        """)
        cmd = input("输入选项：")
        if cmd == '1':
            s.send(cmd.encode())
        elif cmd == '2':
            s.send(cmd.encode())
        elif cmd == '3':
            s.send(cmd.encode())
        else:
            print("请输入正确选项")

if __name__=='__mian__':
    main()