import random

traffic = open('/home/yafet/data/traffic.dat', 'a')

for i in range (720):
	x= random.randrange(1000, 3000, 1)
	print x
	traffic.write("%i\t%i\n" %(i, x))

traffic.close()