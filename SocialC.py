#made by @tannercherry

print (raw_input('Please enter what number in the Fibonacci sequence you would like: '))
input = raw_input('Please enter what number in the Fibonacci sequence you would like: ')

x = 0
oneBack = 1

for x in range(input):
	while x < 2:
		y = 1
	twoBack = oneBack
	oneBack = y
	y = oneBack - twoBack
	x = x - 1

print ('The number is ' + y)