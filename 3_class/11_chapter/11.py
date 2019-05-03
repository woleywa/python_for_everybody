### Read in file, initiate sum ###
import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_198359.txt"
handle = open(name)
sum = int()

for line in handle :
	x=0 ## initiate / reset counter for summing up values
	number = re.findall('([0-9]+)',line) ## extract all the numbers and put in list
	if number: ## check if array has values
		num_length = len(number) ## check length of array
		while x<num_length: ## loop through until end of array
			sum = sum + int(number[x]) ## turn the list value into integer and add to 'sum'
			print(number[x])
			x = x+1 ## increment x
		## wait = input("PRESS ENTER TO CONTINUE.")
print(sum)
