#fname = input("Enter file name: ")
fname = "mbox-short.txt"
# if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = int(0)
for line in fh :
	# if "From:" in line: continue
	if "From" in line and ("From:" or "david.horwitz@uct.ac.za") not in line:
		count += 1
		x = line.rstrip().split()
		print(x[1])
print("There were", count, "lines in the file with From as the first word")
