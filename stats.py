#!/usr/bin/env python3


__author__ = 'dk2ab'

import time
from Parser import Parser
from ContestStats import ContestStats
 
file_name = '121125-cqwwcw.ADI'
file_name = '2009-September.adi'

l = Parser.parseADIF(file_name)
s = ContestStats(l)
print(len(l))

print(s.qsosByBand())
print(s.qsosByOperator())
rph = s.ratesPerHour()
for hour in sorted(rph.keys()):
    print('%s -> %s' % (time.asctime(hour), rph[hour]))
