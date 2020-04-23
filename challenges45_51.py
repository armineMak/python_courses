# 045

# total_var = 0
# while True:
# 	user_input = int(input("please add a number: "))
# 	total_var = user_input + total_var
# 	if total_var <= 50: 
# 		print("the total is: ", total_var)		
# 	elif total_var > 50:
# 		print("it's over 50")
# 		break

# 046

# user_input = 0
# while user_input <= 5:
# 	user_input = int(input("please enter a number: "))
# print("the last added number is a: ", user_input)

# 047

# user_input = int(input("please input a number: "))
# num_sum = user_input
# user_input_other = "y"

# while user_input_other == "y" or user_input_other == "Y": 
# 	enter_num = int(input("please enter number: "))
# 	user_input_other = input("do you whan to add another nuber? y/n: ")
# 	num_sum = num_sum + enter_num
# print("Your total: ", num_sum)

# 048

# member_count = 0

# while True:
# 	invite_smb = input("please enter a party memeber name: ")
# 	print(invite_smb, "has been invited")
# 	user_answer = input("Do you want to invite smbd_else else? Enter y or n: ") 
# 	if user_answer == "y":
# 		member_count = member_count + 1
# 	elif user_answer == "n":
# 		print(member_count, "people are invited to the party.")	
# 		break
# 	else:
# 		print("error!!!")
# 		break


# 049

# comp_num = 50
# count = 0

# while True:
# 	enter_num = int(input("please enter a number: "))
# 	count = count + 1 
# 	if enter_num < comp_num:
# 		print("the entered number is too LOW! please try again!")
# 	elif enter_num > comp_num:
# 		print("the entered number is too HIGH! please try again!")
# 	elif enter_num == comp_num:
# 		print("Well done, you enter", count, "attempts.")
# 		break


# 050

# while True:
# 	user_input = int(input("please input number between 10 and 20: "))
# 	if user_input < 10:
# 		print("Too low! please try again")
# 	elif user_input > 20:
# 		print("Too high! please try again")
# 	elif user_input >= 10 or user_input <=20:
# 		print("Thank you!!")
# 		break


# 051

# bottles_num = 10

# while bottles_num > 0:

# 	print("There are", bottles_num, "green bottles hanging on the wall.")
# 	print(bottles_num, "green bottles hanging on the wall.")
# 	print("And if 1 green bottle aaashould accidently fall")

# 	bottles_num = bottles_num - 1
# 	bottles_left = int(input("How many green bottles will be hanging on the wall? "))

# 	if bottles_left == bottles_num:
# 		print("There will be", bottles_num, "green bottles hanging on the wall")
# 		# break
# 	else:
# 		while bottles_left != bottles_num:
# 			bottles_left = int(input("No, try again: "))
# print("There are no more green bottles hanging on the wall!")
