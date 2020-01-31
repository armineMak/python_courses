def hotel_cost(hotel, nights):

	if hotel == "charlotte":
		return 183 * nights
	elif hotel == "tampa":
		return 455 * nights
	elif hotel == "pittsburgh":
		return 220 * nights
	elif hotel == "los angeles":
		return 500 * nights

hotel = str(input("hotel name: "))
nights = int(input("nights: "))

print(hotel_cost(hotel, nights))