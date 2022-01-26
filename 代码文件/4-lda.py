from typing import TextIO
#import Ipython
import pyLDAvis as pyLDAvis
import pyLDAvis.gensim
import jieba, os, re
from gensim import corpora, models, similarities
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#读取处理好的文本
outfilename = open(r"C:\Users\ZHAOSONGLEI\Desktop\舆情语料\train\result_jieba.txt",'r',encoding='utf-8')

#构建词频矩阵
#train是列表套列表，
train = [[word.strip() for word in line.split()] for line in outfilename]
dictionary = corpora.Dictionary(train)
dictionary.filter_extremes(no_below=5)#去掉频次小于5的词

# corpus[0]: [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1),...]
# corpus是把每条事件ID化后的结果，每个元素是事件中的每个词语，在字典中的ID和频率
corpus = [dictionary.doc2bow(text) for text in train]
print('特征数目: %d' % len(dictionary))
print('文档数目: %d' % len(corpus))

#训练LDA模型
num_topics = 8
eval_every = None
temp = dictionary[0]
id2word = dictionary.id2token

lda = models.LdaModel(corpus=corpus, id2word=dictionary.id2token, num_topics=num_topics, iterations=400, chunksize=2000, passes=20, random_state=None)
topic_list = lda.print_topics(8)
print("8个主题的单词分布为：\n")
for topic in topic_list:
    print(topic)

#可视化
data = pyLDAvis.gensim.prepare(lda, corpus, dictionary, sort_topics=False, mds='mmds')
#pyLDAvis.save_html(data, 'lda_pass10.html')
pyLDAvis.show(data)
pyLDAvis.save_html(data, 'lda_pass10.html')
pyLDAvis.display(data)
#图中圆圈代表不同的主题,圆圈的大小代表主题的重要程度,圆圈越大表示该主题对应数据来说更重要。如果圆圈之间有相互重叠则说明它们所代表的主题有相似之处。