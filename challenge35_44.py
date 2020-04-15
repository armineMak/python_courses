# 041

# user_input = input("please input your name: ")
# user_num = int(input("please input number: "))
# if user_num < 10:
# 	for i in range(0,user_num):
# 		print(user_input)
# else:
# 	for i in range(0,3):
# 		print("Too high")

# 042

# var_total = 0 
# for i in range(0,5):
# 	user_input = int(input("please input numbers 1-5: "))
# 	include_num = input("do you whant to include this number to the total? Y/N: ")
# 	if include_num == "Y" or include_num == "y":
# 		var_total = var_total + user_input
# 		print("Your included total is: ", var_total)
# 	elif include_num == "N" or include_num == "n":
# 		print("Your total is: ", var_total)

# 043

# dir_count = input("please say in what direction you want to count? up/down: ")
# if dir_count == "up":
# 	user_input = int(input("please input the top number: "))
# 	for i in range(1, user_input +1):
# 		print(i)
# elif dir_count == "down":
# 	user_input = int(input("please input a number below 20: "))
# 	for i in range(20, user_input-1, -1):
# 		print(i)
# else: 
# 	print("I don't understand!!")

# 044

# user_input = int(input("please say how many people do you want to invite to the party?: "))

# if user_input < 10:
# 	for i in range(0, user_input):
# 		user_names = input("please enter your guests names: ")
# 		print(user_names, "has been invited to your party!!")
# elif user_input >= 10:
# 	print("Too many people!!")