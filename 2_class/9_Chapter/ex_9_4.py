###
### Ask for file name and read in file
###
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
###
### Split lines, creat dictionary with key / value pair, incr. value for every occurence of key
### 
for line in handle :
	if "From" in line and "From:" not in line:
		key = line.rstrip().split()[1]
		## key = row[1]
		counts[key]=counts.get(key,0)+1
		print(counts[key])

### Loop through the counts dictionary and find the k/v-pair with the highest occurence ###
bigword = None
bigcount = None
for key,value in counts.items(): 
	if bigcount is None or bigcount < value:
		bigcount = value
		bigword = key

print(bigword,bigcount)