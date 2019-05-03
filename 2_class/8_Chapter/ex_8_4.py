# fname = input("Enter file name: ")
fname = "romeo.txt"
fh = open(fname)
lst = list()
count = float(0)
for line in fh:
	x = line.rstrip().split()
	for word in x:
		if word in lst: continue
		lst.append(word)
lst.sort()	
print(lst)
