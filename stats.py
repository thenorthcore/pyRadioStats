#!/usr/bin/env python3
import re
 
file_name = '121125-cqwwcw.ADI'

#src http://web.bxhome.org/blog/ok4bx/2012/05/adif-parser-python 
def parse_adif(fn):
    raw = re.split('<eor>|<eoh>(?i)',open(fn).read() )
    raw.pop(0)  #remove header
    raw.pop()   #remove last empty item
    log =[]
    for record in raw:
         qso = {}
         tags = re.findall('<(.*?):(\d+).*?>([^<\t\n\r\f\v\Z]+)',record)
         for tag in tags:
                qso[tag[0].lower()] = tag[2][:int(tag[1])]
         log.append(qso)    
    return log
#endsrc

def find_operators(log):
	pass

l = parse_adif(file_name)
print(l[0])
print(len(l))
