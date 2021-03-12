class processor:
    def __init__(self,reader,writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)
    def converter(self,data):
        assert False,'converter is not defined'

class HTMLize(processor):
    def converter(self,data):
        return ('<RPE>%s</RPE>' % data.rstrip())+'\n'

html = HTMLize(open('test.txt','r',encoding='utf8'),open('data.txt','w',encoding='utf8'))
html.process()


