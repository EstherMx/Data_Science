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


# # Breaking out of a while loop (infinite loop)
# # Esther's code
# while True: 
#     line = input('>') # ('>') means it takes any input by the user
#     if line != 'done':
#         print(line)
#     else: 
#         print('DONE!')
#         break  #<==== end of the while loop
# print('Outside of the loop')

# # The code
# while True:
# 	line = input('>')
# 	if line == 'done':
# 		print('DONE!')
# 		break # <=== end of the while loop when break is activated
# 	print(line)  # <=== part of the while loop while true
# print('Outside of the loop') # <=== outside of the while loop. called when the loop is over

#In Python, a loop ends a line before indented, compared to javaScript where everything is aligned

#ie:
# n = 0
# while True:
# 	if n == 3:
# 		break
# 	print(n)
# 	n = n + 1  # result: 0 1 2

# In this ie, we start with 0 and as long as n is not equal to 3 we add
# 1 to n and this new n is pushed back up to the while loop 
# until n = 3 and hits the break, which is the end of the loop. NO parentheses
# no curly brakets, no semicolon



# Find the smallest value from a list of values.

# smallest = None
# print('Before:', smallest)
# for itervar in [3, 41,12,9,74,15]:
# 	if smallest is None or itervar < smallest:
# 		smallest = itervar
# 	print('Loop:', itervar, smallest)
# print('Smallest number:', smallest)


#Comment calculer la moyenne de cette array:
# arr = [2, 4, 6, 8, 7, 5]

# moyenne = 0
# quantity = 0
# for chiffre in arr:
# 	moyenne += chiffre
# 	quantity += 1
# moyenne /= len(arr) 
# print('moyenne:',moyenne, 'quantity:', quantity)

# found = False
# for value in [5, 6, 3, 4, 7, 3]:
# 	if value == 3:
# 		found = True
# 		print("here's found:", value, found)
		# found = False
# 		continue
# 	print(found, value)


smallest = None
print(smallest)
for value in [3, 5, 4, 5, 1, 7, 23]:
	if smallest is None or value < smallest:
		smallest = value
print('smallest value:', smallest)
print(id(None))



# LISTS AND STRINGS

From email@gmail.com Sat 12-31-22  #this is a line from the file mbox.txt

#in the python file, we'll write this to import mbox.txt
fhand = open('mbox.txt')  #file name is quotes
for line in fhand:
	line = line rstrip()  #erease the empty space at the end of each line
	if not line startwith('From') : continue #si la ligne du file ne commence pas par 'From' ignore la suite de cette commande
	words = line split() #each line will be returned into an array and the spaces will divide the indexes
	print(words[1]) # returns email@gmail.com




# Find and count the most used words in a file

current_file = open('info.txt')
current_file.rstrip()
count_word = dict()
# divide into words
# loop through every word in the file
# add each word to the dictionary + count
# print the dictionary and class by desc
for word in current_file:
	if word in count_word:
		count_word[word] = count_word[word] + 1
	else count_word[word] = 1
	# or a simpler way instead of the if/else
	count_word[word] = count_word.get(word, 0) + 1
print(count_word)
