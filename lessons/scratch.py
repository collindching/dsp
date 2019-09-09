import os
import re
import csv
from collections import Counter

os.chdir("/Users/collindching/Documents/dsp/lessons/data")
os.getcwd()

from collections import defaultdict

# open file to write
with open("faculty.csv",'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)

    dic = defaultdict(list)
    for r in reader:
        names = tuple(r[0].split())
        dic[names] = r[1:]

print(dic)




d = {}
d[('p','a','d')] = 1
print(d)

