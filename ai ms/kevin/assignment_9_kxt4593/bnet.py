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
        
        firstChar = inputField[0].upper();
        secondChar = inputField[1].lower();
		
        if firstChar == 'B' and secondChar == 't':
            burglary = True
        elif firstChar == 'B' and secondChar == 'f':
            burglary = False

        if firstChar == 'E' and secondChar == 't':
            earthquake = True
        elif firstChar == 'E' and secondChar == 'f':
            earthquake = False

        if firstChar == 'A' and secondChar == 't':
            alarm = True
        elif firstChar == 'A' and secondChar == 'f':
            alarm = False

        if firstChar == 'J' and secondChar == 't':
            jc = True
        elif firstChar == 'J' and secondChar == 'f':
            jc = False

        if firstChar == 'M' and secondChar == 't':
            mc = True
        elif firstChar == 'M' and secondChar == 'f':
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
        final_answer += bn.computeProbability(values[0],values[1],values[2],values[3],values[4],condition)

    print 'P('+str(argv[1:])+') is '+str('%.5f'%final_answer)

if __name__ == '__main__':
	main(sys.argv)
