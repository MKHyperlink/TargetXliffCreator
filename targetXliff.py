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

strings = getStringTable()

for f in root:
    f.attrib['target-language'] = language
    body = f.find(createFullTagName('body'))

    for trans in body.iter(createFullTagName('trans-unit')):
        note = trans.find(createFullTagName('note'))
        if note is not None:
            for s in strings.keys():
                if s in note.text:
                    newEle = etree.Element('target')
                    newEle.text = strings[s].decode('utf-8')
                    trans.insert(trans.index(note), newEle)

nodes.write('%s.xliff'%(language), pretty_print=True, xml_declaration=True, encoding='utf-8')  
