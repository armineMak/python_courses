temp_conv = int(input("please type a temperature: "))
temp_type = str(input("please input type: "))

if temp_type == "F":
	print("the temp in F is: ", (temp_conv * 9/5) + 32, "F")
else: 
	print("the temp in C is: ", temp_conv, "C")
