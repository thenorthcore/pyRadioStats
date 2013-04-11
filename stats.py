#!/usr/bin/env python3


__author__ = 'dk2ab'

from datetime import datetime, timedelta
from Parser import Parser
from ContestStats import ContestStats
 
file_name = '121125-cqwwcw.ADI'
#file_name = '2009-September.adi'

l = Parser.parseADIF(file_name)
s = ContestStats(l)
print(len(l))

print(s.qsosByBand())
print(s.qsosByOperator())
rph = s.ratesPerHour()
for hour in sorted(rph.keys()):
    print('%s -> %s' % (hour, rph[hour]))
print(s.qsosByMode())
print(s.prefixes())
conteststart = datetime.strptime('201211240000', '%Y%m%d%H%M')
contestend = datetime.strptime('201211252359', '%Y%m%d%H%M')

bt = s.breakTimes(conteststart, contestend, timedelta(minutes=60))
sumoff = timedelta(0)
print(bt)
for b in bt:
    print('%s -> %s = %s' % (b['start'], b['end'], b['diff']))
    sumoff += b['diff']

print('Sum offtime: %s' % sumoff)
print('Sum ontime: %s' % ((contestend-conteststart)-sumoff))