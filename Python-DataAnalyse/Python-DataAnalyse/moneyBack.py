def whichCoinsDoIGive(amount, denominationList):
	listLength = len(denominationList)
	possibilities = 0
	for i in range(listLength):
		pos = listLength-1-i
		denomination = denominationList[pos]
		if denomination < amount:
			possibilities += whichCoinsDoIGive(amount-denomination, denominationList[:listLength-i])
			continue
		if denomination == amount:
			possibilities += 1
			continue

	return possibilities

def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]

    return ways_of_doing_n_cents[amount]