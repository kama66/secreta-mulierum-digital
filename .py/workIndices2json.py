import json
from bs4 import BeautifulSoup as bs

#read index file and create soup
def readFile(xmlFile):
    with open(xmlFile, encoding='utf-8') as fp:
        soup = bs(fp, features="lxml-xml", from_encoding="utf-8")
    
    return soup

#create dict to export to json
def xmlToJson(soup):
        allWorks = {}

        for p in soup.find_all("bibl"):
            id = p['xml:id']
            pubD = ""
            author = []
            altNames = []
            varNames = []
            textRef = []
            normLinks = []
            note = []
            for child in p.children:
                   authDict = {}
                   linkDict = {}
                   refDict = {}
                   if child is not None:
                        if child.name == "title":
                            t = child['type']
                            if t == "alt":
                                altNames.append(child.text)
                            if t == "SMvar":
                                varNames.append(child.text)
                            elif t == "reg":
                                regName = child.text

                        if child.name == "idno":
                             linkDict[child['subtype']] = child.text
                             normLinks.append(linkDict)

                        if child.name == "author":
                             authDict[child['ref'][1:]] = child.text
                             author.append(authDict)

                    
                        if child.name == "list" and child['type'] == "textRef":
                            for c in child.children:
                                if c.name == "item":
                                    pg = c.text.split("Seite ", 1)[1]
                                    refDict[c.text] = pg
                            textRef.append(refDict)
                            

                        if child.name == "date":
                            pubD = child.text
                        
                        if child.name == "note":
                            note = child.text
                        
            workDict = {"workID": id, "regName": regName,  "altName": altNames,  "smVar": varNames, "author": author, "date": pubD, "normData": normLinks,  "textRef": textRef, "note": note}
            allWorks[id] = workDict

        writeFile(allWorks)
        
        return

#write out json file
def writeFile(jsonFile):
    with open("works.json", mode="w+", encoding="utf-8") as writeFile:
        json.dump(jsonFile, writeFile)
    return

def main():
    personFile = input("Enter filepath to work index: ")
    xmlTree = readFile(personFile)
    xmlToJson(xmlTree)
    
    return

main()