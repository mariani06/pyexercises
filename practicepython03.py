#Take a list, then prints out all the elements of the list that are less than input number.
a = [1,1,2,3,5,8,13,21,34,55,89]
x = int(raw_input("Input number: "))
#done in one-line
#print([el for el in a if el < x])
b = []
for el in a:
	if el < x:
		b.append(el)
print b
c = raw_input("")