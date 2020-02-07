
user_input = int(input("items count you want: "))
user_items = []
market_stock = ["item1", "item2", "item3"]
available_items = []

for i in range(user_input):
	it_em = input("enter name: ")
	user_items.append(it_em)

for it_em in user_items:
	if it_em in market_stock:
		available_items.append(it_em)

print(available_items)


