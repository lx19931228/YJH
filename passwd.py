import getpass
import hashlib

pwd = getpass.getpass('PASSWD：')
print(pwd)
#hash对象
#hash= hashlib.md5()
#加盐
hash = hashlib.md5('*#123_'.encode()) #生成hash对象
hash.update(pwd.encode())#算法加密
pwd = hash.hexdigest()#提取加密
