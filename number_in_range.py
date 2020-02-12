def my_check_func ():
	my_list = []
	lenght_of_list = int(input("Enter how many items should be in your range: "))
	for i in range(lenght_of_list):
		ele = int(input("Input your items: "))
		my_list.append(ele)
	print(my_list)
	if my_number in my_list:
		print(my_number, " is in range")
	else:
		print("Your number is not in my range")
my_number = int(input("Input your number: "))
my_check_func()