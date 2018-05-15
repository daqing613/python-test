#!/usr/bin/env python
# coding=utf-8

from lxml import etree
from StringIO import StringIO
from collections import defaultdict


def parseXML_to_list(xmlFile):
    """
    Parse the xml
    """
    f = open(xmlFile)
    xml = f.read()
    f.close()

    context = etree.iterparse(StringIO(xml))

    nodes_info = []
    node_dict = {}

    for action, elem in context:
        if elem.text is not None:
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]
                if elem.tag.lower() == "cpumax":
                    node_dict['cpu_max'] = elem.text
                if elem.tag.lower() == "cpuused":
                    node_dict['cpu_used'] = elem.text
                if elem.tag.lower() == "memorymax":
                    node_dict['memory_max'] = elem.text
                if elem.tag.lower() == "memoryused":
                    node_dict['memory_used'] = elem.text
                if elem.tag.lower() == "cpunode":
                    node_dict['cpu_physical'] = elem.text
                if elem.tag.lower() == "clusterid":
                    node_dict['cluster_id'] = elem.text
        if elem.tag == "item":
            nodes_info.append(node_dict)
            node_dict = {}

    return nodes_info


def sum_nodes_info(xml):

    nodes_info = parseXML_to_list(xml)
    nodes_dict = defaultdict(list)
    for node_dict in nodes_info:
        # form dictionaries by cluster_id.
        nodes_dict[(node_dict['cluster_id'])].append(
            {k: v for k, v in node_dict.items() if k != 'cluster_id'})

    def dsum(lists):
        ret = defaultdict(int)
        for d in lists:
            for k, v in dict(d).items():
                ret[k] += int(v)
        return dict(ret)

#    for k, v in dict(nodes_dict).iteritems():
#        print dsum(v)

    result_dict = {k: dsum(v) for k, v in dict(nodes_dict).items()}
    print result_dict


if __name__ == "__main__":
    sum_nodes_info("nodesinfo.xml")
