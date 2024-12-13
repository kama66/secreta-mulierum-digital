import json
import glob
import re
from lxml import html

#write output file
def writeJSON(indexDict):
    with open("pgIndex.json", mode="w+", encoding="utf-8") as write_file:
                   json.dump(indexDict, write_file, indent=2)
    return

#read html file and create tree
def readFile(htmlFile):
    with open(htmlFile, "r", encoding="utf-8") as file: 
        htmlCont = file.read() 
        tree = html.fromstring(htmlCont)

    return tree

#sorting function adapted from https://stackoverflow.com/a/12093995
def sortFiles(value):
      numbers = re.compile(r'(\d+)')
      parts = numbers.split(value)
      parts[1::2] = map(int, parts[1::2])
      return parts

#get all page numbers
def getTitles(tree, indexDict):
        heads = tree.findall(".//div[@class='transcriptionContent']")
        for d in heads:
            pageEl = d.get('id')
            pbId = re.search(r'^pg_\d+', pageEl).group()
            pageId = re.search(r'\d+$', pbId).group()         

            indexDict[pageId] = pbId
            
        return indexDict

def main():
    indexDict = {}
    htmlFileDir = input("Enter filepath to relevant html files: ")
    for file in sorted(glob.glob(htmlFileDir), key=sortFiles):
        jsonDict = getTitles(readFile(file), indexDict)
    writeJSON(jsonDict)
    
    return

main()