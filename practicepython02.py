#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
num = int(raw_input("Input the number: "))
if num%2 == 0:
	if num%4 == 0:
		print(str(num)+" is an even number and multiple of 4")
	else:
		print(str(num)+" is even number")
else:
  print(str(num)+" is odd number")
  
#Extra:
check = int(raw_input("Input number to be divided by num: "))
if check%num == 0:
	print(str(check)+" is divided evenly by "+str(num))
else:
	print(str(check)+" is not divided evenly by "+str(num))