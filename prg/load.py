import re
class geometry:
    def __init__(self,filepath):
        self.filepath = filepath
        #parse geometry file
        #first read file 
        a = load(filepath,'r')
        b = a.read()
        #correct for blank lines in description
        # def eliminate_blanks(text):
        #     if text.find('\n\nEND DESCRIPTION:') == -1:
        #         text.replace('\n\nEND DESCRIPTION:','\nEND DESCRIPTION:')
        #         eliminate_blanks(text)
        #     else:
        #         return text
        # c = eliminate_blanks(b)
        # #define object list by seperating blank lines
        # d = c.split('\n\n')
        delimeters = 'Geom','\nRivers','\nType','\nChan','\nUse'
        regexpattern = '|'.join(map(re.escape,delimeters))
        c = re.split(regexpattern, b)
        title = [x for x in c if x[0:3] == 'Geom']
        rivers = [x for x in c if x[0:3] == 'Rive']
        nodes = [x for x in c if x[0:3] == 'Type']
        chan = [x for x in c if x[0:3] == 'Chan']
        use = [x for x in c if x[0:3] == ''] 
    
        
        
def load(filepath):
    return geometry(filepath)
