structPath = 'struct'
programPath = 'main'
f = open(structPath, 'rb')  # 打开struct文件
f2 = open(programPath, 'rb')  # 打开待反编文件
w_all = f2.read()  # 先读取待反编文件原来的内容
f2.seek(0)  # 读取完之后从头开始
w = f.read(16).hex()  # 再读取16个字节用于比较
w2 = f2.read(16).hex()  # struct也读取16个用于比较
print(w, w2, sep='\n')  # 打印出来让我们看见
add = input('Please input the codes you need to write:')  # 然后问你要在开头写入什么
# 把普通字符串转换为bytes格式，并不是encode，而是fromhex(),把字符串看成是十六进制编码
add = bytes.fromhex(add)
f2.close()  # 关闭
f2 = open(programPath+'.pyc', 'wb')  # 创建pyc待反编文件
f2.write(add+w_all)  # 把加入的字节和原来的字节合并写入文件
f.close()
f2.close()
print('Done.')
