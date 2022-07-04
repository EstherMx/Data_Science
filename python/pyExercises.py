try:
	hours = input("How many hours have you worked?")
	rate = input("How much are you paid an hour?")
except:
	print('this is not a number')
try:
	pay = int(hours) * int(rate)
except: 
	print('enter a number')	
	quit()


print('Pay:', pay)

# Rewrite your pay computation to give 1.5 times the hourly rate for hours worked above
# 40 hours.
if int(hours) > 40:
	overTime = int(hours) - 40
	overTime *= 1.5 * int(rate)
print ('OverTime pay:', overTime)

