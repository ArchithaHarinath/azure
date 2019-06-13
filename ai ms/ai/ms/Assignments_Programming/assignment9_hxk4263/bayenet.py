class BayeNet(object):
	def computeProbability(self, b, e, a, j, m):
		result = (self.P("B",b,None,None) * self.P("E",e,None,None) * self.P("A|B,E",a,b,e) * self.P("J|A",j,a,None) * self.P("M|A",m,a,None))
		return result

	def P(self,query,value1,value2,value3):
		if query == "B":
			if value1:
				return 0.001
			else:
				return 0.999

		if query == "E":
			if value1:
				return 0.002
			else:
				return 0.998

		if query == "A|B,E":
			if value2 and value3:
				temp = 0.95
			if value2 and not value3:
				temp = 0.94
			if not value2 and value3:
				temp = 0.29
			if not value2 and not value3:
				temp = 0.001
			if value1:
				return temp
			else:
				return (1-temp)

		if query == "J|A":
			if value2:
				temp = 0.9
			else:
				temp = 0.05
			if value1:
				return temp
			else:
				return (1-temp)

		if query == "M|A":
			if value2:
				temp = 0.7
			else:
				temp = 0.01
			if value1:
				return temp
			else:
				return (1-temp)

	def enum(self,var):
		if not None in var:
			return self.computeProbability(var[0],var[1],var[2],var[3],var[4])
		else:
			noneIdx = var.index(None)
			new_var = list(var)
			new_var[noneIdx] = True
			val1 = self.enum(new_var)
			new_var[noneIdx] = False
			val2 = self.enum(new_var)
			return val1 + val2

	def genVal(self,var):
		result = []
		if "Bt"	in var:
			result.append(True)
		elif "Bf" in var:
			result.append(False)
		else:
			result.append(None)
		if "Et"	in var:
			result.append(True)
		elif "Ef" in var:
			result.append(False)
		else:
			result.append(None)
		if "At"	in var:
			result.append(True)
		elif "Af" in var:
			result.append(False)
		else:
			result.append(None)
		if "Jt"	in var:
			result.append(True)
		elif "Jf" in var:
			result.append(False)
		else:
			result.append(None)
		if "Mt"	in var:
			result.append(True)
		elif "Mf" in var:
			result.append(False)
		else:
			result.append(None)
		return result

from sys import argv

given = False
obs = []
q = []
for i in range(1,len(argv)):
	if argv[i] == "given":
		given = True
		continue
	q.append(argv[i])
	if given:
		obs.append(argv[i])

bayenet = BayeNet()

if q:
	num = bayenet.enum(bayenet.genVal(q))
	if obs:
		den = bayenet.enum(bayenet.genVal(obs))
	else:
		den = 1
	print "Probability = %.9f" % (num/den)
else:
	print "Invalid query string"
