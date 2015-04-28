# # -*- coding: utf-8 -*-

import lxml.etree as Parser, os
from lxml import etree

from sys import argv

if (len(argv) == 4):
    script, baseFile, srcFile, language = argv
else:
    print 'Arguments amount wrong!'
    print '[base_file] [source_file] [target_language]'
    exit()

nodes = Parser.parse(baseFile)
root = nodes.getroot()


def createFullTagName(text):
    return "{urn:oasis:names:tc:xliff:document:1.2}" + text

def getStringTable():
    strMap = {}
    with open(srcFile) as myfile:
        for line in myfile:
            name, var = line.partition("=")[::2]
            strMap[name.strip('"')] = var.strip()[1:-2]
            # print '[%s]' %strMap[name.strip('"')]
    return strMap

stringTable = getStringTable()

for f in root:
    f.attrib['target-language'] = language
    body = f.find(createFullTagName('body'))

    for trans in body.iter(createFullTagName('trans-unit')):
        note = trans.find(createFullTagName('note'))
        target = trans.find(createFullTagName('target'))
        source = trans.find(createFullTagName('source'))
        if target is None:
            containedStr = None

            for key in stringTable.keys():
                if note is not None and key in note.text:
                    containedStr = key
                    break;
                
            newEle = etree.Element('target')
            if containedStr is not None:
                newEle.text = stringTable[key].decode('utf-8')
            else:
                newEle.text = source.text.decode('utf-8')
            trans.insert(trans.index(source)+1, newEle)


nodes.write('%s.xliff'%(language), pretty_print=True, xml_declaration=True, encoding='utf-8')  
