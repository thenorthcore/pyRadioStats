#!/usr/bin/env python3
import re
import time
 
file_name = '121125-cqwwcw.ADI'
file_name = '2009-September.adi'

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

def RatesPerHour(log):
	ratesPerHour = {}
	for qso in log:
		t = time.strptime(qso['qso_date']+qso['time_on'][0:2], '%Y%m%d%H')
		if t in ratesPerHour:
			ratesPerHour[t] += 1
		else:
			ratesPerHour[t] = 1
	return ratesPerHour

def QSOsByOperator(log):
	qsosByOperator = {}
	for qso in log:
		if qso['operator'] in qsosByOperator:
			qsosByOperator[qso['operator']] += 1
		else:
			qsosByOperator[qso['operator']] = 1
	return qsosByOperator

def QSOsByBand(log):
	qsosByBand = {}
	for qso in log:
		if qso['band'] in qsosByBand:
			qsosByBand[qso['band']] += 1
		else:
			qsosByBand[qso['band']] = 1
	return qsosByBand

l = parse_adif(file_name)
print(len(l))

print(QSOsByBand(l))
print(QSOsByOperator(l))
rph = RatesPerHour(l)
for hour in sorted(rph.keys()):
	print('%s -> %3i' % (time.asctime(hour), rph[hour]))
