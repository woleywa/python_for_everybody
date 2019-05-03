hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
r = float(rate)
if h<41 :
	pay=h*r
else :
	ot=h-40
	pay=(h-ot)*r+ot*(1.5*r)
print(pay)
