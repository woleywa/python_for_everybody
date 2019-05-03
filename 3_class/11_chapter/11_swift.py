### Read in file, initiate sum ###
import re
# results = list(map(int, output))
print(sum(list(map(int, re.findall(r'[0-9]+',open("regex_sum_198359.txt").read())))))
# print(sum(results))

# output = list(map(int,re.findall(r'[0-9]+',name))

## my_list = [int(s) for s in name.split() if s.isdigit()]
## print(my_list)

## print(name.read())



### [int(s) for s in str.split() if s.isdigit()]
