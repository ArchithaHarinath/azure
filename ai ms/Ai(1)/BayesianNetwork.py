class BayesianNetwork:
    giveProbabilities = {}
    probBurglary = 0.001
    probEarthquake = 0.002
    giveProbabilities['MT'] = {'AT':0.70,'AF':0.01}
    giveProbabilities['JT'] = {'AT':0.90,'AF':0.05}
    giveProbabilities['AT'] = {'BT_ET':0.95,'BT_EF':0.94,'BF_ET':0.29,'BF_EF':0.001}


    def computeProbability(self, burglary, earthquake, alarm, john, mary, conditions):
        prob_jc = 0.00
        prob_mc = 0.00
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
                prob_jc = self.giveProbabilities['JT']['AT']
            else:
                prob_jc = 1 - self.giveProbabilities['JT']['AT']
            if mary:
                prob_mc = self.giveProbabilities['MT']['AT']
            else:
                prob_mc = 1 - self.giveProbabilities['MT']['AT']
        else:
            if john:
                prob_jc = self.giveProbabilities['JT']['AF']
            else:
                prob_jc = 1 - self.giveProbabilities['JT']['AF']
            if mary:
                prob_mc = self.giveProbabilities['MT']['AF']
            else:
                prob_mc = 1 - self.giveProbabilities['MT']['AF']

        if burglary and earthquake:
            if alarm:
                pAlarm = self.giveProbabilities['AT']['BT_ET']
            else:
                pAlarm = 1 - self.giveProbabilities['AT']['BT_ET']
        if (not burglary) and earthquake:
            if alarm:
                pAlarm = self.giveProbabilities['AT']['BF_ET']
            else:
                pAlarm = 1 - self.giveProbabilities['AT']['BF_ET']
        if burglary and (not earthquake):
            if alarm:
                pAlarm = self.giveProbabilities['AT']['BT_EF']
            else:
                pAlarm = 1 - self.giveProbabilities['AT']['BT_EF']
        if (not burglary) and (not earthquake):
            if alarm:
                pAlarm = self.giveProbabilities['AT']['BF_EF']
            else:
                pAlarm = 1 - self.giveProbabilities['AT']['BF_EF']

        for condition in conditions:
            if condition == 'B':
                den*=burglary_new
            if condition == 'E':
                den*=earthquake_new
            if condition == 'A':
                den*=pAlarm
            if condition == 'J':
                den*=prob_jc
            if condition == 'M':
                den*=prob_mc

        num = (prob_jc*prob_mc*pAlarm*burglary_new*earthquake_new)
        return num/den