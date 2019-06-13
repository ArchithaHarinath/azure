import sys

class Hyp:
	def __init__(self, p, c, l):
		self.p = p
		self.c = c
		self.l = l

def main():
	if (len(sys.argv) > 2):
		print '[USAGE] python pp.py <Observation String>'
		sys.exit(0)
	r_file = open('result.txt', 'w')
	h1 = Hyp(0.1, 1.0, 0.0)
	h2 = Hyp(0.2, 0.75, 0.25)
	h3 = Hyp(0.4, 0.5, 0.5)
	h4 = Hyp(0.2, 0.25, 0.75)
	h5 = Hyp(0.1, 0.0, 1.0)
	if (len(sys.argv) != 2):
		try:
			r_file.write('Observation sequence Q: \n');
			r_file.write('Length of Q: 0\n\n');
			r_file.write("P(h1 | Q) = %.5f \n" %(h1.p))
			r_file.write("P(h2 | Q) = %.5f \n" %(h2.p))
			r_file.write("P(h3 | Q) = %.5f \n" %(h3.p))
			r_file.write("P(h4 | Q) = %.5f \n" %(h4.p))
			r_file.write("P(h5 | Q) = %.5f \n\n" %(h5.p))
			r_file.write("Probability that the next candy we pick will be Cherry, given Q: 0.50000\n")
			r_file.write("Probability that the next candy we pick will be Lime, given Q: 0.50000\n")
			r_file.close()
		except Exception:
			print 'Error creating a file'
			r_file.close()
		sys.exit(0)
	obs = sys.argv[1]
	obs_len = len(obs)
	count_c = 0
	count_l = 0
	new_p = 0.0
	qC0 = 0.0
	qL0 = 0.0
	r_file.write('Observation sequence Q: '+obs+' \n');
	r_file.write('Length of Q: %d\n' %obs_len);
	for i in xrange(0, obs_len):
		qC0 = (h1.p*h1.c) + (h2.p*h2.c) + (h3.p*h3.c) + (h4.p*h4.c) + (h5.p*h5.c)
		qL0 = (h1.p*h1.l) + (h2.p*h2.l) + (h3.p*h3.l) + (h4.p*h4.l) + (h5.p*h5.l)
		if (obs[i] == 'c' or obs[i] == 'C'):
			if(i == 0):
				new_p = ( (h1.c * h1.p) / qC0);
				h1.p = new_p
				new_p = ( (h2.c * h2.p) / qC0);
				h2.p = new_p
				new_p = ( (h3.c * h3.p) / qC0);
				h3.p = new_p
				new_p = ( (h4.c * h4.p) / qC0);
				h4.p = new_p
				new_p = ( (h5.c * h5.p) / qC0);
				h5.p = new_p
				count_c = count_c + 1;
				r_file.write("\nAfter Observation %d" %(i+1))
				r_file.write(" = " + obs[i]+":\n")
				r_file.write("\nP(h1 | Q) = %.5f \n" %(h1.p))
				r_file.write("P(h2 | Q) = %.5f \n" %(h2.p))
				r_file.write("P(h3 | Q) = %.5f \n" %(h3.p))
				r_file.write("P(h4 | Q) = %.5f \n" %(h4.p))
				r_file.write("P(h5 | Q) = %.5f \n\n" %(h5.p))
			else:
				r_file.write("Probability that the next candy we pick will be Cherry, given Q: %.5f \n" %(qC0))
				r_file.write("Probability that the next candy we pick will be Lime, given Q: %.5f \n" %(qL0))
				new_p = ( (h1.c * h1.p) / qC0);
				h1.p = new_p
				new_p = ( (h2.c * h2.p) / qC0);
				h2.p = new_p
				new_p = ( (h3.c * h3.p) / qC0);
				h3.p = new_p
				new_p = ( (h4.c * h4.p) / qC0);
				h4.p = new_p
				new_p = ( (h5.c * h5.p) / qC0);
				h5.p = new_p
				count_c = count_c + 1;
				r_file.write("\nAfter Observation %d" %(i+1))
				r_file.write(" = " + obs[i]+":\n")
				r_file.write("\nP(h1 | Q) = %.5f \n" %(h1.p))
				r_file.write("P(h2 | Q) = %.5f \n" %(h2.p))
				r_file.write("P(h3 | Q) = %.5f \n" %(h3.p))
				r_file.write("P(h4 | Q) = %.5f \n" %(h4.p))
				r_file.write("P(h5 | Q) = %.5f \n\n" %(h5.p))
		elif (obs[i] == 'l' or obs[i] == 'L'):
			if(i == 0):
				new_p = ( (h1.l * h1.p) / qL0);
				h1.p = new_p
				new_p = ( (h2.l * h2.p) / qL0);
				h2.p = new_p
				new_p = ( (h3.l * h3.p) / qL0);
				h3.p = new_p
				new_p = ( (h4.l * h4.p) / qL0);
				h4.p = new_p
				new_p = ( (h5.l * h5.p) / qL0);
				h5.p = new_p
				count_l = count_l + 1;
				r_file.write("\nAfter Observation %d" %(i+1))
				r_file.write(" = " + obs[i]+":\n")
				r_file.write("P(h1 | Q) = %.5f \n" %(h1.p))
				r_file.write("P(h2 | Q) = %.5f \n" %(h2.p))
				r_file.write("P(h3 | Q) = %.5f \n" %(h3.p))
				r_file.write("P(h4 | Q) = %.5f \n" %(h4.p))
				r_file.write("P(h5 | Q) = %.5f \n\n" %(h5.p))
			else:
				r_file.write("Probability that the next candy we pick will be Cherry, given Q: %.5f \n" %(qC0))
				r_file.write("Probability that the next candy we pick will be Lime, given Q: %.5f \n" %(qL0))
				new_p = ( (h1.l * h1.p) / qL0);
				h1.p = new_p
				new_p = ( (h2.l * h2.p) / qL0);
				h2.p = new_p
				new_p = ( (h3.l * h3.p) / qL0);
				h3.p = new_p
				new_p = ( (h4.l * h4.p) / qL0);
				h4.p = new_p
				new_p = ( (h5.l * h5.p) / qL0);
				h5.p = new_p
				count_l = count_l + 1;
				r_file.write("\nAfter Observation %d" %(i+1))
				r_file.write(" = " + obs[i]+":\n")
				r_file.write("P(h1 | Q) = %.5f \n" %(h1.p))
				r_file.write("P(h2 | Q) = %.5f \n" %(h2.p))
				r_file.write("P(h3 | Q) = %.5f \n" %(h3.p))
				r_file.write("P(h4 | Q) = %.5f \n" %(h4.p))
				r_file.write("P(h5 | Q) = %.5f \n\n" %(h5.p))
		else:
			print 'The inputs can only be a combination of C/c or L/l'
			r_file.close();
			sys.exit(0)
	qC0 = (h1.p*h1.c) + (h2.p*h2.c) + (h3.p*h3.c) + (h4.p*h4.c) + (h5.p*h5.c)
	qL0 = (h1.p*h1.l) + (h2.p*h2.l) + (h3.p*h3.l) + (h4.p*h4.l) + (h5.p*h5.l)
	try:
		r_file.write("Probability that the next candy we pick will be Cherry, given Q: %.5f \n" %(qC0))
		r_file.write("Probability that the next candy we pick will be Lime, given Q: %.5f \n" %(qL0))
	except Exception:
		print 'Error creating a file'
		r_file.close()

if (__name__ == '__main__'):
	main()
