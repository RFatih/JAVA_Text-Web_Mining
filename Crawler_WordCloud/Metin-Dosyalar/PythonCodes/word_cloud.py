import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


def transform_format(val):
    if val == 0:
        return 255
    else:
        return val


df = pd.read_csv("/home/fatih/Desktop/Metin-Dosyalar/Outputs/TableCSV.csv")
del df['web_sayfasi']
print(df.head())

stopwords = set(STOPWORDS)
stopwords.update(["of", "in","the"])

deu_mask = np.array(Image.open("/home/fatih/Desktop/Metin-Dosyalar/PythonCodes/deu.png"))
transformed_deu_mask = np.ndarray((deu_mask.shape[0],deu_mask.shape[1]), np.int32)

for i in range(len(deu_mask)):
    transformed_deu_mask[i] = list(map(transform_format, deu_mask[i]))



tuples = [tuple(x) for x in df.values]

wordcloud = WordCloud(stopwords=stopwords,mask=transformed_deu_mask, max_words=1000, background_color="white",contour_width=3, contour_color='blue').generate_from_frequencies(dict(tuples))

wordcloud.to_file("/home/fatih/Desktop/Metin-Dosyalar/Outputs/deu_output.png")

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


