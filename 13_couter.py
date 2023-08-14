rom collections import Counter
import numpy as np


#words_list = []
with open("sample.txt", "r") as f:
    read = f.read()
    words_lists = read.split()
   # words_list = np.array(words_lists)

counts = Counter(words_lists)

print(counts)
