###
### Ask for file name and read in file
###
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hour_counts = dict()
###
### Split lines, creat dictionary with key / value pair, incr. value for every occurence of key
### 
for line in handle :
	if "From" in line and "From:" not in line:
		key = line.split()[5] ## key extracts the whole timestampe
		hour = key.split(':')[0] ## select the hours from the timestamp
		hour_counts[hour]=hour_counts.get(hour,0)+1 ## create a count for the hours in a dictionary
for key,value in sorted(hour_counts.items()): 
	print(key,value)
		
### print ("key:",key,"hour:",hour,"hour counts:",hour_counts,"keycounts:",counts[key])
# print sorted(hour_counts.items())
# print sorted(hour_counts.items())
### Loop through the counts dictionary and find the k/v-pair with the highest occurence ###
