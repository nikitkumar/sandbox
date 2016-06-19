#!/usr/bin/python
""" Script to play open an FPLC data file and plot UV280
    Usage: $ ./fplcplot1 [file]
	 Note: input files must be tab delimited """

import fileinput
# Initialize arrays
ml = []
mau = []

# collect switches to True onces file headers are skipped
collect = False
i = 0

# Begin reading file and input data into arrays after headers
for line in fileinput.input():
	rawline = line.split() # Splits string line into a list
	i += 1
	if collect and (len(rawline) > 0):
		ml.append(float(rawline[0]))
		mau.append(float(rawline[1]))
	elif (len(rawline) > 0) and line.startswith('ml'):
		collect = True
	else:
		if i == 5:
			collect = True


#Plotting the data
import matplotlib.pyplot as plt
ylimit = max(mau)*1.1
plt.xlim(min(ml), max(ml))
plt.ylim(min(mau),ylimit)
plt.xlabel('mL')
plt.ylabel('mAu')
#plt.title('FPLC Trace')
plt.plot(ml, mau)
plt.grid(True)
plt.show()
#plt.savefig('fplcplot.png')