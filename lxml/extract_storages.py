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


#    storagemax = 0
#     storage_dict = {}

    tree = etree.parse(StringIO(xml))



 #  getroot means.

    root = tree.getroot()

    storages_list = []
    for node in root:
        childs = node.getchildren()
        for elems in childs:
            storage_dict = {}
            for sub_elem in elems:
                if '}' in sub_elem.tag:
                    sub_elem.tag = sub_elem.tag.split('}', 1)[1]
                for tags in ['storageName', 'clusterId', 'storageType', 'spaceMax', 'spaceUsed']:
                    if sub_elem.tag == tags:
                        storage_dict[sub_elem.tag] = sub_elem.text
            if storage_dict['storageType'] != 'ceph':
                pass
            else:
                storages_list.append({k: v for (k, v) in storage_dict.items() if k != 'storageType'})
    print storages_list




# Specify the element item list index .
#    body = tree.xpath("//*[local-name() = 'item']")[0]
#    for elem in body:
#        if '}' in elem.tag:
#            elem.tag = elem.tag.split('}', 1)[1]
#            for tags in ['storageName', 'clusterId', 'spaceMax', 'spaceUsed']:
#                if elem.tag == tags:
#                    storage_dict[elem.tag] = elem.text
#    print storage_dict



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
    parseXML("storages_pro.xml")
