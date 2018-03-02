#-*-coding=utf-8 -*-
import os
#列出某个文件夹下的所有 case,这里用的是 python，
#所在 py 文件运行一次后会生成一个 pyc 的副本
caselist=os.listdir('E:\git\python-learn\src\test-case')
pycachedir='E:\git\python-learn\src\test-case\\__pycache__'
if os.path.exists(pycachedir):
    #删除文件，可使用以下两种方法。
    os.remove(pycachedir)
    #os.unlink(pycachedir)
else:
    print('no such dir:%s'%pycachedir)
    
    
for a in caselist:
    print(a)
    s=a.split('.')[1] 
    #选取后缀名为 py 的文件
    if s=='py':
    #此处执行 dos 命令并将结果保存到 log.txt
        os.system('E:\git\python-learn\src\test-case\\%s 1>>log.txt 2>&1'%a)