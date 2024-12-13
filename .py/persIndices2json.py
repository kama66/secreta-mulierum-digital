import json
from bs4 import BeautifulSoup as bs

#read index file and create soup
def readFile(xmlFile):
    with open(xmlFile, encoding='utf-8') as fp:
        soup = bs(fp, features="lxml-xml", from_encoding="utf-8")
    
    return soup

#create dict to export to json
def xmlToJson(soup):
        allPersons = {}

        for p in soup.find_all("person"):
            id = p['xml:id']
            birthD = ""
            deathD = ""
            altNames = []
            varNames = []
            textRef = []
            relWorks =[]
            normLinks = []
            for child in p.children:
                   
                   linkDict = {}
                   workDict = {}
                   refDict = {}
                   if child is not None:
                        if child.name == "persName":
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

                    
                        if child.name == "list" and child['type'] == "textRef":
                            for c in child.children:
                                if c.name == "item":
                                    pg = c.text.split("Seite ", 1)[1]
                                    refDict[c.text] = pg
                            textRef.append(refDict)
                                
                        if child.name == "listBibl":
                            for c in child.children:
                                if c.name == "bibl":
                                    workDict[c['source'][1:]] = c.text
                            relWorks.append(workDict)

                        if child.name == "birth":
                            birthD = child.contents[1].text
                        if child.name == "death":
                            deathD = child.contents[1].text

            persDict = {"personID": id, "regName": regName,  "altName": altNames,  "smVar": varNames,  "birth": birthD,  "death": deathD, "normData": normLinks,  "works": relWorks,  "textRef": textRef}
            allPersons[id] = persDict

        writeFile(allPersons)
        
        return

#write out json file
def writeFile(jsonFile):
    with open("persons.json", mode="w+", encoding="utf-8") as writeFile:
        json.dump(jsonFile, writeFile)
    return

def main():
    personFile = input("Enter filepath to person index: ")
    xmlTree = readFile(personFile)
    xmlToJson(xmlTree)
    
    return

main()
