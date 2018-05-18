#!/usr/bin/env python
# coding=utf-8


from lxml import etree
from StringIO import StringIO
#----------------------------------------------------------------------



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
    # count =
    # for tag in count:
    #     print tag.text
    run_count = 0
    stop_count = 0
    ter_count = 0
    count = 0
    # body = tree.xpath("//*[local-name() = 'instanceId']")
    body = tree.xpath("//*[local-name() = 'name']")
    for elem in body:
        count += 1
        if elem.text == "running":
            run_count += 1
        elif elem.text == "stopped":
            stop_count += 1
        elif elem.text == "terminated":
            ter_count += 1
    print run_count
    print stop_count
    print ter_count
    print count

#    storagemax = 0



#     tree = etree.parse(StringIO(xml))
#    context = etree.iterparse(StringIO(xml), tag='item')
#    for action, elem in context:
#        storagetype_tag = elem.findall("./storageType")
#        for tag in storagetype_tag:
#            print tag.text
#            for node in elem:
#                spacemax_list = node.findall(".//spaceMax")
#                for spacemax in spacemax_list:
#                    if spacemax.text is not None:
#                        storage_dict[tag] = tag.text
#    print(storage_dict)
#
#     for item in tree.findall('./item'):
#         print("the len is " + len(item))
#         storagetype = item.find('storageType')
#         if storagetype is not None:
#             storagetype = storagetype.text
#             storage_dict['storageType'] = storagetype
#             print " => " + storagetype
#         else:
#             storagetype = None
#
#         spacemax = item.find('spaceMax')
#         if spacemax is not None:
#             spacemax = spacemax.text
#             storage_dict['storageMax'] = spacemax
#             print " => " + spacemax
#         else:
#             spacemax = None
#
#         spaceused = item.find('spaceUsed')
#         if spaceused is not None:
#             spaceused = spaceused.text
#             storage_dict['storageUsed'] = spaceused
#             print " => " + spaceused
#         else:
#             spaceused = None
#         storage_info.append(storage_dict)
#
#         print storage_dict




#    context = etree.iterparse(StringIO(xml))
#    storage_dict = {}
#    storages = []
#
#    for _, elem in context:
#        if not elem.text:
#            text = "None"
#        else:
#            text = elem.text
#            if '}' in elem.tag:
#                elem.tag = elem.tag.split('}', 1)[1]
#                print elem.tag + " => " + text
#                storage_dict[elem.tag] = text
#                if elem.tag == "item":
#                    storages.append(storage_dict)
#                    storage_dict = {}
#    print storages


if __name__ == "__main__":
    parseXML("instances_pro.xml")
