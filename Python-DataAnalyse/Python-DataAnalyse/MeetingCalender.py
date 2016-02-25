def whenCanAMeetingTakePlace(meetingTimes):
	meetingTimes.sort()
	totalMeetingList = [meetingTimes[0]]
	i = 0
	while i < len(meetingTimes):
		totalListLength = len(totalMeetingList)-1
		if meetingTimes[i][0] <= totalMeetingList[totalListLength][1]:
			totalMeetingList[totalListLength] = (totalMeetingList[totalListLength][0], max(meetingTimes[i][1], totalMeetingList[totalListLength][1]))
		else:
			totalMeetingList.append(meetingTimes[i])
		i+=1

	return totalMeetingList
