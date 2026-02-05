print("0b开头是二进制，0o开头是八进制，0x开头是十六进制，打印的时候python都会转为为十进制在转换")

print(0b1101)
print(0o1701)
print(0xa1e1)

print("十进制转为其他字符串都是转为字符串打印")
print("十进制转为二进制",bin(26))
print("十进制转为八进制",oct(26))
print("十进制转为十六进制",hex(26))

print("其他进制换位整型打印出来的也是整型 转换的时候要使用2 8 16指明是几进制")
print(type(int('0b1101',2)))
print(type(int('0o1701',8)))
print(type(int('0xa1e1',16)))


