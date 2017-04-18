#a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old
import datetime
now = datetime.datetime.now()

name = raw_input("What's your name? ")
age = int(raw_input("How old will you be this year? "))
year = now.year + (100-age)

#Extra: Add on to the previous program by asking the user for another number and printing out that many copies of the previous message
#on separate lines.
loop = int(raw_input("How many copies do you want to print it? "))
print(loop * (name+", you'll be 100 yo in "+str(year)+"\n"))