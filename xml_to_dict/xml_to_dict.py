
import xml.etree.ElementTree as ET, re
from collections import defaultdict

class XMLtoDict(object):

    def parse(self, xml):
        return self.__to_dict(ET.fromstring(xml))
    
    def value_from_nest(self, pattern, nest):
        nest = nest if type(nest) is dict else self.parse(nest)
        for k, v in nest.items():
            match = re.search(pattern, k)
            if match:
                return v
            else:
                if type(v) is dict:
                    return self.value_from_nest(pattern, v)

    def __to_dict(self, t):
        d = {t.tag: {} if t.attrib else None}
        children = list(t)
        if children:
            dd = defaultdict(list)
            for dc in map(self.__to_dict, children):
                for k, v in dc.items():
                    dd[k].append(v)
            d = {t.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.items()}}
        if t.attrib:
            d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
        if t.text:
            text = t.text.strip()
            if children or t.attrib:
                if text:
                    d[t.tag]['#text'] = text
            else:
                d[t.tag] = text
        return d