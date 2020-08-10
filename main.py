import xml.etree.ElementTree as ET


class Parser:
    def __init__(self, name):
        self.tree = ET.parse(name)
        self.root = self.tree.getroot()
        self.iter_ = self.tree.iter()

    def parse_it(self):
        for elem in self.iter_:
            print(elem.tag,elem.attrib)


obj = Parser('api_53-004.xml')
obj.parse_it()
