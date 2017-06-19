import sys
import csv
# I had to import the requests library for the HTTP GET command
import requests
# I had to specify this particular function from the library
# The erroc catching didn't work without it
from requests.exceptions import ConnectionError

print "This program will make a call to every url in the supplied csv file. It will output the status code for the failed requests and, at the end, a summary of the successes, fails, and unreachable URLs."
print "Unreachable websites make the program seem like it's hanging. It's not. "
# Global variables to count each good, bad, and unreachable request
globCountGood = 0
globCountBad = 0
globCountN = 0
 
def writeURLs(stringCode, imp, st):
     if ('Unreachable' in stringCode or stringCode.startswith('4') or stringCode.startswith('5')):
         print "For tacticID: " + imp
         print "URL: " + st
         print "returned: " + stringCode
 
# This function counts how many good and bad GET requests are received
# This logic had to be seperated from making the request because if statements don't nest well inside of try/except statements 
# NOTE: 1xx respones are ignored
# The input is the HTTP status code
def countingFunc(stringCode):
    #checking to see if the request code is 2xx or 3xx and updating       the count
    if (stringCode.startswith('2') or stringCode.startswith('3')):
        global globCountGood
        globCountGood += 1
        stringCount = str(globCountGood)
        return stringCount
    #checking to see if the request is 4xx or 5xx and updating the        count
    elif (stringCode.startswith('4') or stringCode.startswith('5')):
        global globCountBad
        globCountBad += 1
        stringCount = str(globCountBad)
        return stringCount
 
# This function makes the HTTP request and gets the status code. 
# This function also checks to see if the site is unreachable  
# The input for the function is the impression pixel from the given dataset 
def getAPIResp(st, imp):
    # This line cleans up the input from the given dataset
    st = st.translate(None, '[]\'\"\\')
    # This is where the request is made and, if successful, the request is passed on to the counting function
    try: 
        r = requests.head(st)
        code = r.status_code
        stringCode = str(code)
        stringCount = countingFunc(stringCode)
    # Here's where the program checks to see if the site is unreachable. If so, a counter for unreachable sites is updated and a NULL entry is recorded
    except:
        stringCode = 'Unreachable'
        global globCountN
        globCountN += 1
        stringCount = str(globCountN)
    stringCode = writeURLs(stringCode, imp, st)
    #print stringCode
    # Writing the failed URLs to the output sheet
#    if (stringCode.startswith('4') or stringCode.startswith('5')):
#        stringCode = stringCode + "," + stringCount + ","+ st + "\n"
    return stringCode        

# The main function
# The CSV file is opened and read. The function then checks to see if there are multiple pixel URLS and either splits them into a list of URLs or passes the single URL to be processed
dataFile = sys.argv[1]
with open(dataFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
        impPixel = row[8]
        tacticID = row[1]
        if "http" in impPixel:
            if "," in impPixel:
                split_up = impPixel.split(',')
                for item in split_up:
                    api = getAPIResp(item, tacticID)
                else:
                    api = getAPIResp(impPixel, tacticID)  
    print "The number of successful GETs:" + str(globCountGood)
    print "The number of failed GETs:" + str(globCountBad)
    print "The number of unreachable sites is: " + str(globCountN)         
                    


    
