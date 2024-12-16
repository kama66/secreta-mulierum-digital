import json
import glob
import re
from lxml import html

#write output file
def writeJSON(indexDict):
    with open("chapIndex.json", mode="w+", encoding="utf-8") as write_file:
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


#get all chapter headings and corresponding page numbers
def getTitles(tree, indexDict):
        heads = tree.findall('.//h3')
        
        for d in heads:
            pageEl = d.get('id')
            pageId = re.search(r'^\d+', pageEl).group()
            pbId = "pg_"+str(pageId)
            chTitle = d.text_content()
            chTitle = re.sub(r"⸗\n+\s*", "", chTitle)
            chTitle = re.sub(r"\d", "", chTitle)
            chTitle = re.sub(r"⸗", "", chTitle)
            chTitle = re.sub(r"\n", " ", chTitle)
            chTitle = re.sub(r"·", " ", chTitle)
            chTitle = re.sub(r"⸫", " ", chTitle)
            chTitle = re.sub(r"⁖", " ", chTitle)
            chTitle = re.sub(r"⁘", " ", chTitle)
            chTitle = re.sub(r"", " ", chTitle)
            chTitle = re.sub(r"…", " ", chTitle)
            chTitle = re.sub(r"-", "", chTitle)
            chTitle = re.sub(r"\.", " ", chTitle)
            chTitle = re.sub(r"⸬", " ", chTitle)
            chTitle = re.sub(r"\s+", " ", chTitle)
            chTitle = re.sub(r"^\s+", "", chTitle)
            chTitle = re.sub(r"\s+$", "", chTitle)

            #print(chTitle.encode("utf-8"))
            
            chNum = re.search(r'\d+$', pageEl)
            if chNum is not None:
                  chNum = chNum.group()+". "
            else:
                  chNum = "1. "

            indexDict[chNum+chTitle] = pbId
            
        return indexDict


def main():
    indexDict = {}
    htmlFileDir = input("Enter filepath to relevant html files: ")
    for file in sorted(glob.glob(htmlFileDir), key=sortFiles):
        jsonDict = getTitles(readFile(file), indexDict)
    writeJSON(jsonDict)
    

    return

main()
