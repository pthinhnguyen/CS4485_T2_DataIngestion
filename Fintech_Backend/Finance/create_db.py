from query import *
def toStrDate(date):
	return str(date.date())
def createDB(fromDate, toDate, user ,user1 , user2):
	#first column : fromDate
	#second column : toDate
	#third column : name
	#fourth : number of tweet
	#fifth : avg BTC low
	#sixth : avg BTC high
	#seventh : avg twitter low
	#eighth : avg twitter high
	currentDate = datetime.datetime(fromDate[0], fromDate[1], fromDate[2])
	endDate = datetime.datetime(toDate[0], toDate[1], toDate[2])
	
	fromDateStr = str(datetime.datetime(fromDate[0], fromDate[1], fromDate[2]).date())
	toDateStr = str(datetime.datetime(toDate[0], toDate[1], toDate[2]).date())
	column = np.asarray(["fromDate" , "toDate" ,"name" , "numberOfTweet" , "AVGBTCHigh" , "AVGBTCLow" , "AVGTWTRHigh" , "AVGTWTRLow" , "name1" , "numTweets1" , "name2" , "numTweets2"])
	
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
		r = len(BTCField)
		for data in BTCField:
			sumHigh = sumHigh + data[1]
			sumLow = sumLow + data[2]

		AVGHigh = sumHigh / r
		
		AVGLow = sumLow / r
		row.append(AVGHigh)
		row.append(AVGLow)
		
		#print("r : ",r, " sumHigh : ",sumHigh)
	
		TWTRField = getDataSticker("TWTR" , toStrDate(currentDate) , toStrDate(nextDate))
		sumHigh = 0.0
		sumLow = 0.0
		r = len(TWTRField)
		for data in TWTRField:
			sumHigh = sumHigh + data[1]
			sumLow = sumLow + data[2]

		AVGHigh = sumHigh / r
		
		AVGLow = sumLow / r
		row.append(AVGHigh)
		row.append(AVGLow)
		row.append( user1)
		row.append(len(filterDateTimeAuthor(currentDate, nextDate , user1)))
		row.append(user2)
		row.append(len(filterDateTimeAuthor(currentDate, nextDate , user2)))
		fields.append(row)

		currentDate = nextDate + datetime.timedelta(days=1)
		print("r : ",r, " sumHigh : ",sumHigh)
		if (nextDate == endDate):
			break
		
	
	print(np.asarray(fields))
	frame = pd.DataFrame(np.asarray(fields) , columns = column )
	frame.to_csv('aggregation'+'.csv')

createDB((2021,1,1) , (2022,4,26) , "@elonmusk" , "@JoeBiden" , "@katyperry")
