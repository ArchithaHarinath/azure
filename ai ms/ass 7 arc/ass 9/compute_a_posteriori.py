import sys

class hypo:
    def __init__(self,prior,cherry,lime):
	self.prior = prior
	self.cherry = cherry
	self.lime = lime
def initvar():
    h1 = hypo(0.1,1,0)
    h2 = hypo(0.2,0.75,0.25)
    h3 = hypo(0.4,0.5,0.5)
    h4 = hypo(0.2,0.25,0.75)
    h5 = hypo(0.1,0,1)
    return list([h1,h2,h3,h4,h5])
 
def calculatePjQj_1(h,inputsample):
    result = 0
    for prior_prob in h:
	if inputsample=='C':
            result = result+prior_prob.prior*prior_prob.cherry     	
	else:
	    result = result+prior_prob.prior*prior_prob.lime
    return result

def main(argv): 
    inputsample = argv[1]
    file = open("result.txt","w")
    file.write("Observation sequence Q: "+inputsample)
    file.write("\nLength of Q: "+str(len(inputsample)))
    h = initvar()
    Q = {}
    Q['C'] = calculatePjQj_1(h,'C')
    Q['L'] = 1-Q['C']
    for i in range(0,len(inputsample)):
        file.write("\n\nAfter Observation "+str(i+1)+": "+inputsample[i]+"\n")
        for j in range(0,len(h)):
	    if inputsample[i]=='C':
	        h[j].prior = (h[j].prior*h[j].cherry)/Q['C']
	    else:
		h[j].prior = (h[j].prior*h[j].lime)/Q['L']		
	    file.write("\nP(h"+str(j+1)+"|Q) = "+str(h[j].prior))
	Q['C'] = calculatePjQj_1(h,'C')
	Q['L'] = 1-Q['C']
        file.write("\n\nProbability that the next candy we pick will be C, given Q:"+str(Q['C']))
	file.write("\nProbability that the next candy we pick will be L, given Q:"+str(Q['L']))
    print("Output is printed in result.txt successfully")

if __name__ == '__main__':
    main(sys.argv)
