def hotel_cost(day_price):
	charlotte = 183 
	tampa = 220 
	pittsburgh = 422 
	los_angeles = 475
	return charlotte * day_price, tampa * day_price, pittsburgh * day_price, los_angeles * day_price

day_price = int(input("nights: "))

print(hotel_cost(day_price))

