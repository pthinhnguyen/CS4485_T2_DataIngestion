from query import *
def toStrDate(date):
	return str(date.date())
def createDB(fromDate, toDate, user):
	#first column : fromDate
	#second column : toDate
	#third column : name
	#fourth : number of tweet
	#fifth : avg BTC low
	#sixth : avg BTC high
	currentDate = datetime.datetime(fromDate[0], fromDate[1], fromDate[2])
	endDate = datetime.datetime(toDate[0], toDate[1], toDate[2])
	
	fromDateStr = str(datetime.datetime(fromDate[0], fromDate[1], fromDate[2]).date())
	toDateStr = str(datetime.datetime(toDate[0], toDate[1], toDate[2]).date())
	column = np.asarray(["fromDate" , "toDate" ,"name" , "numberOfTweet" , "AVGBTCHigh" , "AVGBTCLow"])
	
	fields = []
	for i in range(1000000000):
		nextDate = currentDate + datetime.timedelta(days=6)
		if (nextDate > endDate):
			nextDate = endDate
			#open high low
		row = [toStrDate(currentDate)  , toStrDate(nextDate) , user , len(filterDateTimeAuthor(currentDate, nextDate , user))]
		BTCField = getDataSticker("BTC-USD" , toStrDate(currentDate) , toStrDate(nextDate))
		sumHigh = 0.0
		sumLow = 0.0
		r = float((nextDate - currentDate).days)
		for data in BTCField:
			sumHigh = sumHigh + data[1]
			sumLow = sumLow + data[2]

		AVGHigh = sumHigh / r
		
		AVGLow = sumLow / r
		row.append(AVGHigh)
		row.append(AVGLow)
		fields.append(row)
		currentDate = nextDate + datetime.timedelta(days=1)
		if (nextDate == endDate):
			break
	
	print(np.asarray(fields))
	frame = pd.DataFrame(np.asarray(fields) , columns = column )
	frame.to_csv('aggregation'+'.csv')

createDB((2022,1,1) , (2022,4,1) , "@elonmusk")
