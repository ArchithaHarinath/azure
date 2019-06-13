import sys
from copy import *
from BayesianNetwork import *


def createTables(ttable,input_condition):
    if input_condition.count(None) != 0:
        noneIndex = input_condition.index(None)
        t = deepcopy(input_condition)
        t[noneIndex] = True
        f = deepcopy(input_condition)
        f[noneIndex] = False
        createTables(ttable,t)
        createTables(ttable,f)
        return ttable
    else:
        ttable.append(input_condition)
        return ttable

def main(argv):
    
    input_arr = argv[1:]
    
    condition = [];
    burglary = None;
    earthquake = None;
    alarm = None;
    jc = None;
    mc = None;
    for inputField in input_arr:
        
        c1 = inputField[0].upper();
        c2 = inputField[1].lower();
		
        if c1 == 'B' and c2 == 't':
            burglary = True
        elif c1 == 'B' and c2 == 'f':
            burglary = False

        if c1 == 'E' and c2 == 't':
            earthquake = True
        elif c1 == 'E' and c2 == 'f':
            earthquake = False

        if c1 == 'A' and c2 == 't':
            alarm = True
        elif c1 == 'A' and c2 == 'f':
            alarm = False

        if c1 == 'J' and c2 == 't':
            jc = True
        elif c1 == 'J' and c2 == 'f':
            jc = False

        if c1 == 'M' and c2 == 't':
            mc = True
        elif c1 == 'M' and c2 == 'f':
            mc = False
    
    conIndex = 0
    if input_arr.count('given'):
        conIndex = input_arr.index('given')
        for j in range(conIndex+1,len(input_arr)):
            condition.append(input_arr[j][0])
    formattedInput = [burglary,earthquake,alarm,jc,mc];
    denominators = condition;
    
    bn = BayesianNetwork()
    allCombinations = createTables([],formattedInput)
    
    final_answer = 0.00

    for values in allCombinations:
        final_answer =final_answer+ bn.computeProbability(values[0],values[1],values[2],values[3],values[4],condition)

    print 'P('+str(argv[1:])+') is '+str('%.5f'%final_answer)

if __name__ == '__main__':
	main(sys.argv)
