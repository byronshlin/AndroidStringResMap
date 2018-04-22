# coding=utf-8
import csv
import sys
import re
import os

def readFiles(fileName):
    with open(fileName) as f:
        fileLines = f.readlines()
    stringline = []
    pattern = re.compile('<string name=".*".*>.*</string>')
    for line in fileLines:
        stringItem = line.strip()
        result = pattern.match(stringItem)
        if result :
            stringline.append(stringItem)
    return stringline

def getKey(stringItem) :
    index1 = stringItem.find('"')
    index2 = stringItem.find('"',(index1+1), len(stringItem))
    key = stringItem[(index1+1) : index2]
    return key

def getValue(stringItem):
    index1 = stringItem.find(">")
    index2 = stringItem.rfind("</string>")
    value = stringItem[(index1+1) : index2]
    return value

def getStringMap(fileName):
    stringList = readFiles(fileName)
    stringMap = {}
    for stringItem in stringList:
        key = getKey(stringItem)
        value = getValue(stringItem)
        stringMap[key]=[value]
    return stringMap

def listXml(directory):
    files = os.listdir(directory)
    resources = []
    for f in files:
        if f.endswith('.xml'):
            resources.append(f)
    return resources

def scanDirectoryAndGenerateStrings(dirFiles):
    files = listXml(dirFiles)
    strings = {}
    for f in files :
        stringsMap = getStringMap(dirFiles+"/"+f)
        strings.update(stringsMap)
    return strings


def appendDict(destDict, srcDict, key):
    value = srcDict.get(key)
    distList = destDict.get(key)
    if distList is None:
        return
    if type(distList) is not list:
        return

    if value == None:
        distList.append(None)
    else:
        if type(value) is list:
            distList.extend(value)
        else :
            distList.append(value)

def mergetDict(destDict,srcDict):
    keys = destDict.keys()
    for k in keys:
        appendDict(destDict, srcDict, k)
    return destDict

def transferList(stringsDict):
    keys = stringsDict.keys()
    stringsListList = []
    for key in keys:
        value = stringsDict[key]
        stringsList = []
        stringsList.append(key)
        if type(value) is list:
            for v in value:
                stringsList.append(v)
        else :
            stringsList.append(value)
        stringsListList.append(stringsList)
    return stringsListList

def generateCSV(dataList, outputFileName):
    with open(outputFileName, "wt") as output:
        outputWriter = csv.writer(output)
        outputWriter.writerows(dataList)


def generateStringCSV(*argcs):
    try :
        os.remove("output.csv")
    except:
        pass
    mainStrings = scanDirectoryAndGenerateStrings("values")
    titles=['resources', "en"]
    for lang in argcs:
        try:
            localeStrings = scanDirectoryAndGenerateStrings("values-"+lang)
            mainStrings = mergetDict(mainStrings, localeStrings)
            titles.append(lang)
        except:
            pass
    stringsListList = transferList(mainStrings)
    stringsListList.insert(0,titles)
    generateCSV(stringsListList,"output.csv")


def generateStringCSVByArgc(argc):
    params =[]
    argvLen = len(argc)
    print(argvLen)
    if argvLen > 1:
        for i in range(1, argvLen):
            print(i)
            params.append(argc[i])
    else:
        params=["zh-rTW", "in"]
    generateStringCSV(*params)

def main(argv):
    #generateStringCSV("zh-rTW", "in")
    generateStringCSVByArgc(argv)

if __name__ == "__main__":
    main(sys.argv)


#mainStrings = StringsUtils.scanDirectoryAndGenerateStrings("values")
#stringsOfZh = StringsUtils.scanDirectoryAndGenerateStrings("values-zh-rTW")
#stringsOfIn = StringsUtils.scanDirectoryAndGenerateStrings("values-in")
#mainStrings = mergetDict(mainStrings, stringsOfZh)
#mainStrings = mergetDict(mainStrings, stringsOfIn)
#stringsListList = transferList(mainStrings)
#stringsListList.insert(0,['resources', "en", "zh", "in"])
#generateCSV(stringsListList,"output.csv")
