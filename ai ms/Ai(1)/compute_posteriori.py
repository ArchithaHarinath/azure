#Posterior probablity
import sys
#Contains prior probability and respective probabilites of cherry and lime for each hypothesis
class hypothesis:
    def __init__(self,prior,cherry,lime):
	self.prior = prior
	self.cherry = cherry
	self.lime = lime
#initializing all the hypothesis and returning them as a list
def initvar():
    h1 = hypothesis(0.1,1,0)
    h2 = hypothesis(0.2,0.75,0.25)
    h3 = hypothesis(0.4,0.5,0.5)
    h4 = hypothesis(0.2,0.25,0.75)
    h5 = hypothesis(0.1,0,1)
    return list([h1,h2,h3,h4,h5])
 
#returns PjQj+1 value
def calculatePjQj_1(h,s):
    res = 0
    for p in h:
	if s=='C':
            res = res+p.prior*p.cherry     	
	else:
	    res = res+p.prior*p.lime
    return res

def main(argv): 
    s = argv[1]
    f = open("result.txt","w")
    f.write("Observation sequence Q: "+s)
    f.write("\nLength of Q: "+str(len(s)))
    h = initvar()
    Q = {}
    Q['C'] = calculatePjQj_1(h,'C')
    Q['L'] = 1-Q['C']
    #Iterate over each observation and calculate hypothesis probabilities and cherry and lime probability based on the values calculated in previous step
    for i in range(0,len(s)):
        f.write("\n\nAfter Observation "+str(i+1)+": "+s[i]+"\n")
        for j in range(0,len(h)):
	    if s[i]=='C':
	        h[j].prior = (h[j].prior*h[j].cherry)/Q['C']
	    else:
		h[j].prior = (h[j].prior*h[j].lime)/Q['L']		
	    f.write("\nP(h"+str(j+1)+"|Q) = "+str(h[j].prior))
	Q['C'] = calculatePjQj_1(h,'C')
	Q['L'] = 1-Q['C']
        f.write("\n\nProbability that the next candy we pick will be C, given Q:"+str(Q['C']))
	f.write("\nProbability that the next candy we pick will be L, given Q:"+str(Q['L']))
    print("Open result.txt for results")

if __name__ == '__main__':
    main(sys.argv)
