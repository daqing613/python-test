#!/usr/bin/env python
# coding=utf-8


from lxml import etree
from StringIO import StringIO


def parseXML(xmlFile):
    """
    Parse the xml
    """
    f = open(xmlFile)
    xml = f.read()
    f.close()

    tree = etree.parse(StringIO(xml))
    # for child in root:
    #     print child.tag, child.attrib
    # count = tree.findall("{http://ec2.amazonaws.com/doc/2009-08-15/}instanceId")
    # for tag in count:
    #     print tag.text
    count = 0
    body = tree.xpath("//*[local-name() = 'instanceId']")
    for elem in body:
        print elem.tag + " => " + elem.text
        count += 1
    print count


if __name__ == "__main__":
    parseXML("instances.xml")
