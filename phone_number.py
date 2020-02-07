while True:
	try:
		input_num = int(input("please input your number: +374"))
		if len(str(input_num)) != 8:
			print("enter valid length for phone number")
			continue
		operator_id = str(input_num)[:2]
		if operator_id in ["91", "96", "99", "43"]:
			print("your operator is Beeline")
		elif operator_id in ["77", "93", "94"]:
			print("your operator is Viva Cell")
		elif operator_id in ["55", "95"]:
			print("your operator is Ucom")
		else: 
			print("Unkown operator")
		break
	except: 
		print("enter valid phone number")
