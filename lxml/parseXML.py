#!/usr/bin/env python
# coding=utf-8

from lxml import etree, objectify
from StringIO import StringIO

#----------------------------------------------------------------------
def parseXML(xmlFile):
    """
    Parse the xml
    """
    f = open(xmlFile)
    xml = f.read()
    f.close()

    context = etree.iterparse(StringIO(xml))
    cpumax = 0
    cpuused = 0
    memorymax = 0
    memoryused = 0
    for action, elem in context:
        if elem.text is not None:
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]
                if elem.tag.lower() == "cpumax":
                    cpumax += int(elem.text)
                if elem.tag.lower() == "cpuused":
                    cpuused += int(elem.text)
                if elem.tag.lower() == "memorymax":
                    memorymax += int(elem.text)
                if elem.tag.lower() == "memoryused":
                    memoryused += int(elem.text)
    print(cpumax)
    print(cpuused)
    print(memorymax)
    print(memoryused)


if __name__ == "__main__":
    parseXML("nodesinfo.xml")
