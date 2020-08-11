import xml.etree.ElementTree as ET

class Parser:
    def __init__(self, name):
        self.tree = ET.parse(name)
        self.iter_ = self.tree.iter()
        self.functions = {}
        self.bufer = {}

    def parse_childs(self,data):

        if data.getchildren():
            self.bufer[data.attrib['count']] = []
            self.parse_childs(self, data.getchildren())
        else:
            if data.tag=='integer':
                val=0
            elif data.tag=='string':
                val = ''
            elif data.tag=='double':
                val = 1.1
            if data.attrib['name'] in self.bufer:
                self.bufer[data.attrib['name']]=val

    def parse_it(self):
        for elem in self.iter_:
            inp={}
            out={}
            #print(elem.attrib)
            for fn in elem.getchildren():
                if fn.tag=='input':
                    self.bufer={}
                    #print(fn.getchildren())
                if fn.tag == 'output':
                    break
            if 'name' in elem.keys() and 'rpcf_' in elem.attrib['name']:
                self.functions[elem.attrib['name']] = {'id': elem.attrib['id'], 'input': inp,'output': out}
        #print(self.functions)

    def runner(self, attr, *args, **kwargs):
        '''метод, который будет имитировать все прочие методы'''
        function = attr
        if function in self.functions.keys():
            print(function, *args, **kwargs)
        else:
            print('No function found')

    def __getattr__(self,attr):
        def wrap(*args,**kwargs):
            return self.runner(attr,*args,**kwargs)
        return wrap


obj = Parser('api_53-004.xml')
obj.parse_it()
obj.rpcf_get_stats({'type':1235})