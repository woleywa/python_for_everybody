# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
value=float(0)
count=float(0)
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	spos=line.find('0')
	line=float(line[spos:])
	value=value+line
	count=count+1
#	print(count,line,value)
#print("Done")
print("Average spam confidence:",value/count)