# try:
# 	hours = input("How many hours have you worked?")
# 	rate = input("How much are you paid an hour?")
# except:
# 	print('this is not a number')
# try:
# 	pay = int(hours) * int(rate)
# except: 
# 	print('enter a number')	
# 	quit()


# print('Pay:', pay)

# # Rewrite your pay computation to give 1.5 times the hourly rate for hours worked above
# # 40 hours.
# if int(hours) > 40:
# 	overTime = int(hours) - 40
# 	overTime *= 1.5 * int(rate)
# print ('OverTime pay:', overTime)


# Breaking out of a while loop (infinite loop)
# Esther's code
while True: 
    line = input('>') # ('>') means it takes any input by the user
    if line != 'done':
        print(line)
    else: 
        print('DONE!')
        break  #<==== end of the while loop
print('Outside of the loop')

# The code
while True:
	line = input('>')
	if line == 'done':
		print('DONE!')
		break # <=== end of the while loop when break is activated
	print(line)  # <=== part of the while loop while true
print('Outside of the loop') # <=== outside of the while loop. called when the loop is over

#In Python, a loop ends a line before indented, compared to javaScript where everything is aligned

#ie:
n = 0
while True:
	if n == 3:
		break
	print(n)
	n = n + 1  # result: 0 1 2

# In this ie, we start with 0 and as long as n is not equal to 3 we add
# 1 to n and this new n is pushed back up to the while loop 
# until n = 3 and hits the break, which is the end of the loop. NO parentheses
# no curly brakets, no semicolon



# Find the smallest value from a list of values.

smallest = None
print('Before:', smallest)
for itervar in [3, 41,12,9,74,15]:
	if smallest is None or itervar < smallest:
		smallest = itervar
	print('Loop:', itervar, smallest)
print('Smallest number:', smallest)