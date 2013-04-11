__author__ = 'dk2ab'

from datetime import datetime
import re

class ContestStats:

    def __init__(self, log, contestName = None):
        self.log = []
        self.contestName = contestName
        if contestName is not None:
            for entry in log:
                if entry['CONTEST_ID'] == contestName:
                    self.log.append(entry)
        else:
            self.log = log

    def byBand(self, statistic, qso):
        band = qso['band']
        if band in statistic:
            statistic[band] += 1
        else:
            statistic[band] = 1

    def ratesPerHour(self):
        ratesPerHour = {}
        for qso in self.log:
            t = datetime.strptime(qso['qso_date']+qso['time_on'][0:2], '%Y%m%d%H')
            if t not in ratesPerHour:
                ratesPerHour[t] = {}
            self.byBand(ratesPerHour[t], qso)
        return ratesPerHour

    def qsosByOperator(self):
        qsosByOperator = {}
        for qso in self.log:
            op = qso['operator']
            if op not in qsosByOperator:
                qsosByOperator[op] = {}
            self.byBand(qsosByOperator[op], qso)
        return qsosByOperator

    def qsosByBand(self):
        qsosByBand = {}
        for qso in self.log:
            self.byBand(qsosByBand, qso)
        return qsosByBand

    def qsosByMode(self):
        qsosByMode = {}
        for qso in self.log:
            mode = qso['mode']
            if mode not in qsosByMode:
                qsosByMode[mode] = {}
            self.byBand(qsosByMode[mode], qso)
        return qsosByMode

    def prefixes(self):
        prefixes = set()
        for qso in self.log:
            prefix = re.findall('(^[\w]{1,2}[\d]+)', qso['call'])
            assert len(prefix) == 1, "There might be an error in the prefix-regexp (%s, %s)" % (qso['call'], prefix)
            prefixes.add(prefix[0])
        return sorted(prefixes)

    def breakTimes(self, contestStart, contestEnd, minBreak):
        offTimes = []
        tlast = contestStart
        for qso in self.log:
            if len(qso['time_on']) == 4:
                t = datetime.strptime(qso['qso_date']+qso['time_on'], '%Y%m%d%H%M')
            elif len(qso['time_on']) == 6:
                t = datetime.strptime(qso['qso_date']+qso['time_on'], '%Y%m%d%H%M%S')

            tdiff = t - tlast
            if tdiff > minBreak:
                offTimes.append({'start': tlast, 'end': t, 'diff': t - tlast})
            tlast = t

        tdiff = contestEnd - tlast
        if tdiff > minBreak:
            offTimes.append({'start': tlast, 'end': contestEnd, 'diff': contestEnd - tlast})

        return offTimes
