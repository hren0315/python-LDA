from wordcloud import WordCloud
import imageio

import matplotlib.pyplot as plt
output_path = open(r"C:\Users\ZHAOSONGLEI\Desktop\舆情语料\train\result_jieba.txt",'r',encoding='utf-8').read()
text = output_path
mask = imageio.imread("xin.jpg")
wordcloud = WordCloud(font_path="C:/Windows/Fonts/simsun.ttc", background_color="black", width=800, height=600, max_words=150, max_font_size=100, mask=mask).generate(text)
wordcloud.to_file('xin.png')