import csv
import re
#code to find current time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#function to remove emojis from string
def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)
    
# creating menu driven for user input
#give proper file path to open() function
with open('bagbazar.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        columns = row
        break;
    #columns[0] = "sno"
    i = 0;
    for val in columns:
    	print(i," "+val)
    	i = i+1
    choice = input("choose option to print particular data : ")


#reading csv file and appending filtered data
#give proper file path to open() function
with open('bagbazar.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
    	#appending data to customized csv file
    	csvFile = open('filter : '+current_time+".csv",'a')
    	csvWriter = csv.writer(csvFile)
    	if(int(choice) == 8):
    		encoded_string = row[int(choice)].encode("ascii", "ignore")
    		decode_string = encoded_string.decode()
    		csvWriter.writerow([deEmojify(row[int(choice)])])
    	else:
    		string =""
    		for x in row[int(choice)]:
    			string +=x
    		csvWriter.writerow([string])
