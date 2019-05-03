### Read in file, initiate sum ###
import re
name = open("regex_sum_198359.txt").read()
output = re.findall('\D',name)
print(output)
wait = input("Press Enter")	
results = list(map(int, output))
print(results)
wait
print(sum(results))

# output = list(map(int,re.findall(r'[0-9]+',name))

## my_list = [int(s) for s in name.split() if s.isdigit()]
## print(my_list)

## print(name.read())



### [int(s) for s in str.split() if s.isdigit()]
