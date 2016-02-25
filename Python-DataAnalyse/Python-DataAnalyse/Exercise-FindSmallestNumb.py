def findMinInList(numberList):
	minNumber = numberList[0]
	for number in numberList:
		if minNumber > number:
			minNumber = number
	return minNumber

def findKSmallestNumb(numberList, kSmallest):
	minNumberList = [None] * kSmallest
	for number in numberList:
		for pos in range(kSmallest):
			if minNumberList[pos] is None:
				minNumberList[pos] = number
				break
			if minNumberList[pos] <= number:
				continue
			oldNum = minNumberList[pos]
			minNumberList[pos] = number
			number = oldNum
			

	return minNumberList[kSmallest-1]
