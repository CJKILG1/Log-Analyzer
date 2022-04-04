from datetime import date
import re, pickle, os

class LogAnalyzer:
    def __init__(self):
        self.monthDict = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        self.log = ''
        self.globalLogList = []
        self.startDate = ''
        self.endDate = ''
        self.queryNumber = 0
        self.entryAmmount = 0
        self.statusCodeInput = ''
        self.reqestMethodINput = ''
        
        
    def createLogList(self):  
        logDirectory = os.path.join(os.getcwd(), 'log')
        for logFile in os.listdir(logDirectory):
            file = os.path.join(logDirectory, logFile)
            f = open(file, 'r')
            for line in f:
                self.globalLogList.append(str(line))
                
        with open("globalLogList.txt", 'wb') as newFile:
            pickle.dump(self.globalLogList, newFile)
                
    def selectionMenu(self):
        statusCodeRegex = r"([1-5]\d\d)" 
        statusCodeRegexObj = re.compile(statusCodeRegex)
        requestMethodRegex = r'\bOPTIONS\b|\bGET\b|\bHEAD\b|\bPOST\b|\bPUT\b|\bDELETE\b|\bTRACE\b|\bCONNECT\b|\bPATCH\b'
        requestMethodRegexObj = re.compile(requestMethodRegex)
        dateRegex = r"([0-3][0-9]/[A-Z][a-z][a-z]/\d\d\d\d)"
        dateRegexObj = re.compile(dateRegex)
        
        print('Please select a search variable from the following list:'
              + '\nTop Client IP Addresses from a given date range (1)'
              + '\nTop HTTP Request Method from a given date range (2)'
              + '\nTop Client IP Addresses from a given date range with HTTP Status Code (3)'
              + '\nTop Client IP Addresses with both HTTP Status Code and HTTP Request Method (4)'
              + '\nEnter a number between 1 and 4 based on the selection list >>>>' )
        
        while(True):
            userQueryInput = str(input())
            if userQueryInput == '1' or userQueryInput == '2' or userQueryInput == '3' or userQueryInput == '4':
                break
            else:
                print('Please enter a valid input >>>>')
                
        self.queryNumber = int(userQueryInput)
                
        if userQueryInput == '1':
            print('You have chosen to search for the Top Client IP Addresses from a given date range.')
            print('Please enter the ammount of IP Addresses you would like to include in your results >>>>')
            while(True):
                tempInput = input()
                if tempInput.isdigit():
                    self.entryAmmount = int(tempInput)
                    break
                else:
                    print('Please enter a valid input >>>>')
                    
            print('Please enter a starting date in the following format (<day>/<month>/<year>, ex. 01/Jan/2000), or select all time by typing "ALL" >>>>')
            while(True):
                self.startDate = input()
                if self.startDate != 'ALL':
                    matchedDateObj = dateRegexObj.search(self.startDate)
                    try:
                        validInput = str(matchedDateObj.group())
                    except:
                        validInput = 'None'
                    if validInput != 'None':
                        self.startDate = validInput
                        break
                    else:
                        print('Please enter a valid input >>>>')
                else:
                    break
       
            if self.startDate != 'ALL':
                print('Please enter an ending date for your search >>>>')
                while(True):
                    self.endDate = input()
                    matchedDateObj = dateRegexObj.search(self.endDate)
                    try:
                        validInput = str(matchedDateObj.group())
                    except:
                        validInput = 'None'
                    if validInput != 'None':
                        self.endDate = validInput
                        break
                    else:
                        print('Please enter a valid input >>>>')
            else:
                    self.startDate = '01/Jan/1900'
                    self.endDate = '01/Jan/2500'
            
            print('Preparing results from ' + self.startDate + ' to ' +  self.endDate + ' ...')
                    
                
        elif userQueryInput == '2':
            print('You have chosen to search for Top HTTP Request Methods from a given date range.')
            print('Please enter the ammount of HTTP Request Methods you would like to include in your results >>>>')
            while(True):
                tempInput = input()
                if tempInput.isdigit():
                    self.entryAmmount = int(tempInput)
                    break
                else:
                    print('Please enter a valid input >>>>')
    
            print('Please enter a starting date in the following format (<day>/<month>/<year>, ex. 01/Jan/2000), or select all time by typing "ALL" >>>>')
            while(True):
                self.startDate = input()
                if self.startDate != 'ALL':
                    matchedDateObj = dateRegexObj.search(self.startDate)
                    try:
                        validInput = str(matchedDateObj.group())
                    except:
                        validInput = 'None'
                    if validInput != 'None':
                        self.startDate = validInput
                        break
                    else:
                        print('Please enter a valid input >>>>')
                else:
                    break
       
            if self.startDate != 'ALL':
                print('Please enter an ending date for your search >>>>')
                while(True):
                    self.endDate = input()
                    matchedDateObj = dateRegexObj.search(self.endDate)
                    try:
                        validInput = str(matchedDateObj.group())
                    except:
                        validInput = 'None'
                    if validInput != 'None':
                        self.endDate = validInput
                        break
                    else:
                        print('Please enter a valid input >>>>')
            else:
                    self.startDate = '01/Jan/1900'
                    self.endDate = '01/Jan/2500'
            print('Preparing results from ' + self.startDate + ' to ' +  self.endDate + ' ...')
            
        elif userQueryInput == '3':
            print('You have chosen to search for the Top Client IP Addresses with HTTP Status Codes from a given date range.')
            print('Please enter the ammount of Client IP Addresses you would like to include in your results >>>>')
            while(True):
                tempInput = input()
                if tempInput.isdigit():
                    self.entryAmmount = int(tempInput)
                    break
                else:
                    print('Please enter a valid input >>>>')
            print('Please enter an HTTP Status Code (example: 404) >>>>')
            while(True):
                self.statusCodeInput = input()
                matchedStatusCodeInput = statusCodeRegexObj.search(self.statusCodeInput)
                try:
                    validInput = str(matchedStatusCodeInput.group())
                except:
                    validInput = 'None'
                if validInput != 'None':
                    self.startDate = validInput
                    break
                else:
                    print('Please enter a valid input >>>>')   
            
            print('Please enter a starting date in the following format (<day>/<month>/<year>, ex. 01/Jan/2000), or select all time by typing "ALL" >>>>')
            while(True):
                self.startDate = input()
                if self.startDate != 'ALL':
                    matchedDateObj = dateRegexObj.search(self.startDate)
                    try:
                        validInput = str(matchedDateObj.group())
                    except:
                        validInput = 'None'
                    if validInput != 'None':
                        self.startDate = validInput
                        break
                    else:
                        print('Please enter a valid input >>>>')
                else:
                    break
       
            if self.startDate != 'ALL':
                print('Please enter an ending date for your search >>>>')
                while(True):
                    self.endDate = input()
                    matchedDateObj = dateRegexObj.search(self.endDate)
                    try:
                        validInput = str(matchedDateObj.group())
                    except:
                        validInput = 'None'
                    if validInput != 'None':
                        self.endDate = validInput
                        break
                    else:
                        print('Please enter a valid input >>>>')
            else:
                    self.startDate = '01/Jan/1900'
                    self.endDate = '01/Jan/2500'
            print('Preparing results from ' + self.startDate + ' to ' +  self.endDate + ' ...')
            
        elif userQueryInput == '4':
            print('You have chosen to search for the Top Client IP Addresses with HTTP Status Codes and HTTP Request Methods from a given date range.')
            print('Please enter the ammount of Client IP Addresses you would like to include in your results >>>>')
            while(True):
                tempInput = input()
                if tempInput.isdigit():
                    self.entryAmmount = int(tempInput)
                    break
                else:
                    print('Please enter a valid input >>>>')
            print('Please enter an HTTP Status Code (example: 404) >>>>')
            while(True):
                self.statusCodeInput = input()
                matchedStatusCodeInput = statusCodeRegexObj.search(self.statusCodeInput)
                try:
                    validInput = str(matchedStatusCodeInput.group())
                except:
                    validInput = 'None'
                if validInput != 'None':
                    self.startDate = validInput
                    break
                else:
                    print('Please enter a valid input >>>>')   
            print('Please enter an HTTP Request Method (example: POST, GET, etc.) >>>>')
            while(True):
                self.requestMethodInput = str(input()).upper()
                matchedRequestMethodInput = requestMethodRegexObj.search(self.requestMethodInput)
                try:
                    validInput = str(matchedRequestMethodInput.group())
                except:
                    validInput = 'None'
                if validInput != 'None':
                    self.requestMethodInput = validInput
                    break
                else:
                    print('Please enter a valid input >>>>')

                self.requestMethodInput = validInput

        
            print('Please enter a starting date in the following format (<day>/<month>/<year>, ex. 01/Jan/2000), or select all time by typing "ALL" >>>>')
            while(True):
                self.startDate = input()
                if self.startDate != 'ALL':
                    matchedDateObj = dateRegexObj.search(self.startDate)
                    try:
                        validInput = str(matchedDateObj.group())
                    except:
                        validInput = 'None'
                    if validInput != 'None':
                        self.startDate = validInput
                        break
                    else:
                        print('Please enter a valid input >>>>')
                else:
                    break
       
            if self.startDate != 'ALL':
                print('Please enter an ending date for your search >>>>')
                while(True):
                    self.endDate = input()
                    matchedDateObj = dateRegexObj.search(self.endDate)
                    try:
                        validInput = str(matchedDateObj.group())
                    except:
                        validInput = 'None'
                    if validInput != 'None':
                        self.endDate = validInput
                        break
                    else:
                        print('Please enter a valid input >>>>')
            else:
                    self.startDate = '01/Jan/1900'
                    self.endDate = '01/Jan/2500'
            print('Preparing results from ' + self.startDate + ' to ' +  self.endDate + ' ...')
            
    def parseList(self):
        self.createLogList()
        self.selectionMenu()
        dateRegex = r"([0-3][0-9]/[A-Z][a-z][a-z]/\d\d\d\d)"
        dateRegexObj = re.compile(dateRegex)
        ipRegex = r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
        ipRegexObj = re.compile(ipRegex)
        yearRegex = r"([1-2][0-9][0-9][0-9])"
        yearRegexObj = re.compile(yearRegex)
        dayRegex = r"([0-3][0-9])"
        dayRegexObj = re.compile(dayRegex)
        monthRegex = r"([A-Z][a-z][a-z])"
        monthRegexObj = re.compile(monthRegex)
        ipRegex = r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
        ipRegexObj = re.compile(ipRegex)
        statusCodeRegex = r"([ ][1-5]\d\d[ ])" 
        statusCodeRegexObj = re.compile(statusCodeRegex)
        requestMethodRegex = r'\bOPTIONS\b|\bGET\b|\bHEAD\b|\bPOST\b|\bPUT\b|\bDELETE\b|\bTRACE\b|\bCONNECT\b|\bPATCH\b'
        requestMethodRegexObj = re.compile(requestMethodRegex)
        countDict = {}
        
        logDirectory = os.path.join(os.getcwd(), 'log')

        with open("globalLogList.txt", 'rb') as newFile:
                globalLog = pickle.load(newFile)
                
        for log in globalLog:
            matchedDateObj = dateRegexObj.search(log)
            matchedInputMonthObj1 = monthRegexObj.search(self.startDate)
            matchedInputMonthObj2 = monthRegexObj.search(self.endDate)
            matchedGlobalMonthObj = monthRegexObj.search(str(matchedDateObj.group()))

            matchedInputDayObj1 = dayRegexObj.search(self.startDate)
            matchedInputDayObj2 = dayRegexObj.search(self.endDate)
            matchedGlobalDayObj = dayRegexObj.search(str(matchedDateObj.group()))
    
            # CODE TO REMOVE LEADING 0'S FROM DAY NUMBERS
            if matchedInputDayObj1.group()[0] == '0':
                matchedInputDayObj1 = matchedInputDayObj1.group().strip('0')
            else:
                matchedInputDayObj1 = matchedInputDayObj1.group()
            if matchedInputDayObj2.group()[0] == '0':
                matchedInputDayObj2 = matchedInputDayObj2.group().strip('0')
            else:
                matchedInputDayObj2 = matchedInputDayObj2.group()
            if matchedGlobalDayObj.group()[0] == '0':
                matchedGlobalDayObj = matchedGlobalDayObj.group().strip('0')
            else:
                matchedGlobalDayObj = matchedGlobalDayObj.group()

            matchedInputYearObj1 = yearRegexObj.search(self.startDate)
            matchedInputYearObj2 = yearRegexObj.search(self.endDate)
            matchedGlobalYearObj = yearRegexObj.search(str(matchedDateObj.group())) 

            globalDate = date(int(matchedGlobalYearObj.group()), self.monthDict.get(matchedGlobalMonthObj.group()), int(matchedGlobalDayObj))
            startDate1 = date(int(matchedInputYearObj1.group()), self.monthDict.get(matchedInputMonthObj1.group()), int(matchedInputDayObj1))
            endDate1 = date(int(matchedInputYearObj2.group()), self.monthDict.get(matchedInputMonthObj2.group()), int(matchedInputDayObj2))
                
            if globalDate >= startDate1 and globalDate <= endDate1:
                matchedGlobalIpAddressObj = ipRegexObj.match(log)
                matchedGlobalStatusCodeObj = statusCodeRegexObj.search(log)
                statusCodeString = matchedGlobalStatusCodeObj.group()
                statusCodeString = statusCodeString.strip(' ')
                try:
                    matchedGlobalRequestMethod = requestMethodRegexObj.search(log)
                    requestMethodString = str(matchedGlobalRequestMethod.group())
                except:
                    requestMethodString = 'None'
                if self.queryNumber == 1:
                    ipAddressString = str(matchedGlobalIpAddressObj.group())
                    if ipAddressString in countDict:
                        countDict[ipAddressString] += 1
                    else:
                        countDict[ipAddressString] = 0
                elif self.queryNumber == 2:
                    if requestMethodString in countDict:
                        countDict[requestMethodString] += 1
                    elif requestMethodString not in countDict and requestMethodString != 'None':
                        countDict[requestMethodString] = 0
                elif self.queryNumber == 3:
                    ipAddressString = str(matchedGlobalIpAddressObj.group() + ' ' + statusCodeString)
                    if self.statusCodeInput in ipAddressString: 
                        if ipAddressString in countDict:
                            countDict[ipAddressString] += 1
                        else:
                            countDict[ipAddressString] = 0
                elif self.queryNumber == 4:
                    ipAddressString = str(matchedGlobalIpAddressObj.group() + ' ' + requestMethodString + ' ' + statusCodeString)
                    if self.statusCodeInput in ipAddressString and self.requestMethodInput in ipAddressString: 
                        if ipAddressString in countDict:
                            countDict[ipAddressString] += 1
                        else:
                            countDict[ipAddressString] = 0
                            
        sortedLogs = sorted(countDict, key = countDict.get, reverse = True)
        topN = sortedLogs[:self.entryAmmount]
        i = 0
        for log in topN:
            topN[i] = str(topN[i]) + ' (' + str(countDict[log]) + ' entries)'
            i+=1
        
        if len(topN) == 1:
            print('Here is the top entry:\n' + str(topN))
        else:
            print('Here are the top ' + str(len(topN)) + ' entries from most common to least common:\n' + str(topN))

        print('\n\n\n')
        

c1 = LogAnalyzer()
while(True):
    c1.parseList()






