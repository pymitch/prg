import re
class geometry:
    def __init__(self,filepath):
        self.filepath = filepath
        #parse geometry file
        #first read file 
        a = open(filepath,'r')
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
        delimeters = r'\n(?=Rivers)',r'\n(?=Type)',r'\n(?=Chan)',r'\n(?=Use)',
        r'\n(?=)',r'\n(?=Storage Area)',r'\n(?=Connection)',r'\n(?=Pump Station)',r'\n(?=LCMann Time)',
        regexpattern = '|'.join(delimeters)
        c = re.split(regexpattern, b)
        self.c = c
        
        title = [x for x in c if x[0:4] == 'Geom']
        rivers = [x for x in c if x[0:4] == 'Rive']
        nodes = [x for x in c if x[0:4] == 'Type']
        chan = [x for x in c if x[0:4] == 'Chan']
        use = [x for x in c if x[0:3] == 'Use']
        
        nodes_obj = []
        #keys = ['Type RM Length L Ch R','Node Last Edited Time','#Sta/Elev','#Mann','Bank Sta','XS Rating Curve','XS HTab Starting El and Incr','XS HTab Horizontal Distribution','Exp/Cntr']

        for node in nodes:
            delimeters = r'\n(?=Node Last Edited)',r'\n(?=#Sta/Elev)',r'\n(?=#Mann)',r'\n(?=Bank Sta)',
            r'\n(?=XS Rating Curve)',r'\n(?=XS HTAB Starting El and Incr)',r'\n(?=XS HTab Horizontal Distribution)',
            r'\n(?=Exp/Cntr)',r'\n(?=Junc L&A)',r'\n(?=END DESCRIPTION:)', r'\n(?=XS GIS Cut Line)', 
',
            regexpattern = '|'.join(delimeters)
            n = re.split(regexpattern,node)
            
            nodes_obj.append(n)
            


        self.title = [x for x in c if x[0:4] == 'Geom']
        self.rivers = [x for x in c if x[0:4] == 'Rive']
        self.nodes = [x for x in c if x[0:4] == 'Type']
        self.chan = [x for x in c if x[0:4] == 'Chan']
        self.use = [x for x in c if x[0:3] == 'Use']
        
        
    
        
        
def load(filepath):
    return geometry(filepath)
