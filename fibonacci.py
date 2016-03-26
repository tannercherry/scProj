#made by @tannercherry

number = int(input('Please enter what number in the Fibonacci sequence you would like: '))

x = 0
twoBack, oneBack = 1, 1

for x in range(number-1):
	oneBack, twoBack = twoBack, oneBack+twoBack

print ('The number is ', oneBack)