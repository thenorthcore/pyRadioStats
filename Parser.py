__author__ = 'dk2ab'

import re


class Parser:
    @staticmethod
    def parseADIF(file):
        #src http://web.bxhome.org/blog/ok4bx/2012/05/adif-parser-python
        raw = re.split('<eor>|<eoh>(?i)', open(file).read())
        raw.pop(0)  # remove header
        raw.pop()   # remove last empty item
        log = []
        for record in raw:
            qso = {}
            tags = re.findall('<(.*?):(\d+).*?>([^<\t\n\r\f\v\Z]+)', record)
            for tag in tags:
                qso[tag[0].lower()] = tag[2][:int(tag[1])]
            log.append(qso)
        return log
        #endsrc