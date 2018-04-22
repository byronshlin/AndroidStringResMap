import csv
import sys
import re
import os
import getopt



stringListList = []
with open('output.csv', encoding='utf-8') as csvfile:
     spamreader = csv.reader(csvfile)
     for row in spamreader:
         stringListList.append(row)
#print(stringListList)

titles = stringListList[0]

titles = titles[1:]
localizeRes=[]  #[[en...], [zh....]]
files=[]

for t in titles:
    name = "strings-"+t+".xml"
    files.append(name)
    localizeRes.append([])

stringListList = stringListList[1:]


keys = []
for stringList in stringListList:
    size = len(stringList)
    key = stringList[0]
    keys.append(key)

    for i in range(1,size):
        value = stringList[i]
        localizeRes[i-1].append(value)



for index in range(0, len(localizeRes)):
    localizeString = localizeRes[index]
    name = files[index]
    string_out = open(name,'w')
    size = len(keys)
    for i in range(0, size) :
        if localizeString[i] != None and len(localizeString[i]) != 0:
            s = '<string name="{0}">{1}</string>\n'.format(keys[i],localizeString[i])
            string_out.write(s)
    string_out.close()







#if __name__ == "__main__":
#    main(sys.argv)
