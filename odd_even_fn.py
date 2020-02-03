def show_numbers(limit):

	for i in range(limit+1):
		if i % 2 != 0:
			print(i, "ODD")
		else: 
			print(i, "EVEN")

limit = int(input("please input your number: ")) 

show_numbers(limit)