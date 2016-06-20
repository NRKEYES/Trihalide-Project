import re
import sys
import glob



files = glob.glob("output/*.out") # recturns a list of all the .out files in a directory



print 'Energy,R1,R2,A'

for outputFile in files:
	#print outputFile
	outputFile = open(outputFile, 'r')
	outputFile = outputFile.read()
	
	ZPE = re.findall(r'FINAL SINGLE POINT ENERGY     (.*)', outputFile) #Pull ZPE values in Hartree
	if not ZPE:
		continue
	ZPE = ZPE[len(ZPE)-1]
	#print ZPE
	
	R1 = re.findall(r'R1 = (.*)', outputFile)
	R1 = R1[len(R1)-1]


	R2 = re.findall(r'R2 = (.*)', outputFile)
	R2 = R2[len(R2)-1]


	A = re.findall(r'A =(.*)', outputFile)
	A = A[len(A)-1]

	print '%s, %s, %s, %s' %(ZPE, R1, R2, A)

