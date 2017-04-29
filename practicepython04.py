#Asks the user for a number and then prints out a list of all the divisors of that number
a = int(raw_input("Input number: "))
x = range(2, a+1)
b = []
for el in x:
	if a%el == 0:
		b.append(el)
print b