import json
from lxml import html
import re
from pathlib import Path
import glob

def getJsonFile(htmlFile):
    #read file
    with open(htmlFile, "r", encoding="utf-8") as file: 
        htmlCont = file.read() 
        fileName = Path(htmlFile).stem

        #create content tree
        searchTree = html.fromstring(htmlCont)

        #get page and facsimile number information
        d = searchTree.find(".//div[@id]")
        pageEl = d.get('id')
        id = re.search(r'pg_\d+', pageEl).group()
        idNum = re.search(r'\d+', id).group()
        nextId = "pg_"+str(int(idNum)+1) if int(idNum)<244 else None
        prevId = "pg_"+str(int(idNum)-1) if int(idNum)>1 else None
        facs = re.search(r'facs_\d+', pageEl).group()

        #get number of lines
        lineNums = int(searchTree.xpath('count(//br)'))

        #create html string
        treeStr = html.tostring(searchTree.find_class('transcriptionContent')[0], encoding='utf-8').decode('utf-8')
        treeStr = re.sub(r'</div>\n\s+', r'</div>', treeStr)
        
        #write out json file
        with open("./json/"+str(fileName)+".json", mode="w", encoding="utf-8") as write_file:
            json.dump({"id": id, "nextId": nextId, "prevId": prevId, "facs": facs, "format": "json", "lines": lineNums, "content": treeStr}, write_file)
        
    return

def main():
    htmlFileDir = input("Enter filepath to relevant html files: ")
    #get json file for each html file
    for file in glob.glob(htmlFileDir):
        getJsonFile(file)

    return

main()