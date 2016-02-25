def getMaxProfit(stockPriceList):
	currentMinPrice = None
	bestProfit = stockPriceList[1] - stockPriceList[0]
	for price in stockPriceList:
		if currentMinPrice is None:
			currentMinPrice = price
			continue
		calcDifference = price-currentMinPrice
		if bestProfit < calcDifference:
			bestProfit = calcDifference
		if price < currentMinPrice:
			currentMinPrice = price

	return bestProfit

def getMaxProductOfThreeNumbers(input_List):
	listLength = len(input_List)
	
	smallestNumber = None
	biggestNumber = None
	highestProductOf2 = None
	lowestProductOf2 = None
	highestProductOf3 = None
	for number in input_List:
		if smallestNumber is None:
			smallestNumber = number
			continue
		if biggestNumber is None:
			if number > smallestNumber:
				biggestNumber = number
			else:
				biggestNumber = smallestNumber
				smallestNumber = number
			multiplied = smallestNumber*biggestNumber
			highestProductOf2 = multiplied
			lowestProductOf2 = multiplied
			continue
		if highestProductOf3 is None:
			highestProductOf3 = max(highestProductOf2*number, lowestProductOf2*number)
		else:
			highestProductOf3 = max(highestProductOf3, highestProductOf2*number, lowestProductOf2*number)
		highestProductOf2 = max(highestProductOf2, smallestNumber*number, biggestNumber*number)
		lowestProductOf2 = min(lowestProductOf2, smallestNumber*number, biggestNumber*number)
	return highestProductOf3
