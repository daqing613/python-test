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
    cpu_max = 0
    cpu_used = 0
    cpu_physical = 0
    memory_max = 0
    memory_used = 0
    cluster_id = None
    for action, elem in context:
        if elem.text is not None:
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]
                if elem.tag.lower() == "cpumax":
                    cpu_max += int(elem.text)
                if elem.tag.lower() == "cpuused":
                    cpu_used += int(elem.text)
                if elem.tag.lower() == "memorymax":
                    memory_max += int(elem.text)
                if elem.tag.lower() == "memoryused":
                    memory_used += int(elem.text)
                if elem.tag.lower() == "cpunode":
                    cpu_physical += int(elem.text)
                if elem.tag.lower() == "clusterid":
                    cluster_id = elem.text
    print("cpu_max : %s" % cpu_max)
    print("cpu_used : %s" % cpu_used)
    print("cpu_physical : %s" % cpu_physical)
    print("memory_max : %s" % memory_max)
    print("memory_used : %s" % memory_used)
    print("cluster_id : %s" % cluster_id)


if __name__ == "__main__":
    parseXML("nodesinfo.xml")
