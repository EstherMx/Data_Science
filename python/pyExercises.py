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


# Breaking out of a while loop
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