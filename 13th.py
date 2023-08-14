from collections import Counter
import numpy as np


words_list = []
with open("C:/Users/GOKUL SHANTHOSH/Downloads/sample.txt.txt", "r", encoding="utf8" ) as f:
    read = f.read()
    words_list = read.split()
    words_list = np.array(words_list)

counts = Counter(words_list)

print(counts)

