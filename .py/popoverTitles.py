#create modified version of the edition xml file as preparation for website
#the resulting xml is only intended to be used as an intermediary step in the transformation pipeline

from bs4 import BeautifulSoup as bs

#read file and create soup
def readFile(xmlFile):
    with open(xmlFile, encoding='utf-8') as fp:
        soup = bs(fp, features="lxml-xml", from_encoding="utf-8")
    
    return soup

#get titles from indices and add them as attribute values to main xml
def createTitles(sm, refData, attr, el):
    for p in sm.find_all(el):
        author = refData.find(attrs={"xml:id" : p[attr][1:]})
        a = author.find(attrs={"type" : "reg"})
        if el == "persName":
            p['key'] = a.text
        elif el == "bibl":
            p['corresp'] = a.text

    return sm

def writeOut(sm, file):
    with open(file, mode="w+", encoding="utf-8") as writeFile:
         writeFile.write(str(sm))

    return

def main():
    smFile = input("Enter filepath to edition xml file: ")
    persFile = input("Enter filepath to person index: ")
    workFile = input("Enter filepath to work index: ")
    
    smTree = readFile(smFile)
    persTree = readFile(persFile)
    workTree = readFile(workFile)
    smTree = createTitles(smTree, persTree, "ref", "persName")
    smTree = createTitles(smTree, workTree, "source", "bibl")
    writeOut(smTree, smFile)
    
    return

main()