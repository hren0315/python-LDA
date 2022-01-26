import jieba

input_path = r"C:\Users\ZHAOSONGLEI\Desktop\舆情语料\train\result.txt"
output_path = r"C:\Users\ZHAOSONGLEI\Desktop\舆情语料\train\result_jieba.txt"
stopwords_path = "C:\\Users\\ZHAOSONGLEI\\Desktop\\东西\\我的\\stopwords.txt"

# 设置停用词,把停用词放进列表
#print('start read stopwords data.')
stopwords = []
with open(stopwords_path, 'r') as f:
    for line in f:
        if len(line) > 0:
            stopwords.append(line.strip())

#定义分词函数
def tokenizer(s):
    words = []
    cut = jieba.cut(s)
    for word in cut:
        if word not in stopwords:
            if len(word) > 1:
                words.append(word)
    return words

# 读取文件数据，分词，并输出到文件
with open(output_path, 'w',encoding='utf-8') as o:
    with open(input_path, 'r',encoding='utf-8') as f:
        for line in f:
            s = tokenizer(line.strip())
            o.write(" ".join(s) + "\n")

