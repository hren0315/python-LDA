import os

#文件所在文件夹
filedir = r"C:\Users\ZHAOSONGLEI\Desktop\舆情语料\train"

#获取路径下所有文件（包括子目录内的文件），并存入列表
pathss = []
for root, dirs, files in os.walk(filedir):
    path = [os.path.join(root, name) for name in files]
    pathss.extend(path)

#打开result.txt文件，如果没有则创建
f = open(r"C:\Users\ZHAOSONGLEI\Desktop\舆情语料\train\result.txt",'w',encoding='utf-8')

#遍历单个文件，读取行
#写入result文件中
for files in pathss:
    for line in open(files, encoding='utf-8'):
        f.writelines(line)
f.close() #关闭文件


