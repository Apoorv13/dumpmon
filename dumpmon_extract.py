import csv
from collections import defaultdict
import re
import requests
import os

columns = defaultdict(list)

with open('dumpmon_dumpmon.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

urls = columns['text']
length = len(urls)
fin_urls = []
print length
for i in urls:
	temp = re.search("(?P<url>https?://[^\s]+)", i).group("url")
	fin_urls.append(temp)

print fin_urls

for fil in fin_urls:
	r = requests.get(fil)
	#fileName = fil.replace("/","")+".txt"
	#fileName = fileName.replace(":","")+".txt"
	fileName = fil.split("/")
	print fileName[3]+".txt"
	os.system("touch "+fileName[3]+".txt")
	f1 = open(fileName[3]+".txt","wr")
	f1.write(r.text)
	f1.close()
