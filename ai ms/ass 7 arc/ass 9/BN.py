class BN:
    giveProbabilities = {}
    probBurglary = 0.001
    probEarthquake = 0.002
    giveProbabilities['MarryT'] = {'AlarmT':0.70,'AlarmF':0.01}
    giveProbabilities['JohnT'] = {'AlarmT':0.90,'AlarmF':0.05}
    giveProbabilities['AlarmT'] = {'BT_ET':0.95,'BT_EF':0.94,'BF_ET':0.29,'BF_EF':0.001}


    def computeProbability(self, burglary, earthquake, alarm, john, mary, conditions):
        prob_johncalls = 0.00
        prob_marycalls = 0.00
        pAlarm = 0.00
        probability = 1
        burglary_new = 0.00
        earthquake_new = 0.00
        den = 1.00

        if earthquake:
            earthquake_new = self.probEarthquake
        else:
            earthquake_new = 1 - self.probEarthquake

        if burglary:
            burglary_new = self.probBurglary
        else:
            burglary_new = 1 - self.probBurglary

        if alarm:
            if john:
                prob_johncalls = self.giveProbabilities['JohnT']['AlarmT']
            else:
                prob_johncalls = 1 - self.giveProbabilities['JohnT']['AlarmT']
            if mary:
                prob_marycalls = self.giveProbabilities['MarryT']['AlarmT']
            else:
                prob_marycalls = 1 - self.giveProbabilities['MarryT']['AlarmT']
        else:
            if john:
                prob_johncalls = self.giveProbabilities['JohnT']['AlarmF']
            else:
                prob_johncalls = 1 - self.giveProbabilities['JohnT']['AlarmF']
            if mary:
                prob_marycalls = self.giveProbabilities['MarryT']['AlarmF']
            else:
                prob_marycalls = 1 - self.giveProbabilities['MarryT']['AlarmF']

        if burglary and earthquake:
            if alarm:
                pAlarm = self.giveProbabilities['AlarmT']['BT_ET']
            else:
                pAlarm = 1 - self.giveProbabilities['AlarmT']['BT_ET']
        if (not burglary) and earthquake:
            if alarm:
                pAlarm = self.giveProbabilities['AlarmT']['BF_ET']
            else:
                pAlarm = 1 - self.giveProbabilities['AlarmT']['BF_ET']
        if burglary and (not earthquake):
            if alarm:
                pAlarm = self.giveProbabilities['AlarmT']['BT_EF']
            else:
                pAlarm = 1 - self.giveProbabilities['AlarmT']['BT_EF']
        if (not burglary) and (not earthquake):
            if alarm:
                pAlarm = self.giveProbabilities['AlarmT']['BF_EF']
            else:
                pAlarm = 1 - self.giveProbabilities['AlarmT']['BF_EF']

        for condition in conditions:
            if condition == 'B':
                den=den*burglary_new
            if condition == 'E':
                den=den*earthquake_new
            if condition == 'A':
                den=den*pAlarm
            if condition == 'J':
                den=den*prob_johncalls
            if condition == 'M':
                den=den*prob_marycalls

        num = (prob_johncalls*prob_marycalls*pAlarm*burglary_new*earthquake_new)
	return num/den
