import collections
import urllib.request
import re
import collections
def ngram(string, N):
        D = dict()
        N = 2
        strparts = string.split()
        for i in range(len(strparts)-N+1): # N-grams
            try:
                D[tuple(strparts[i:i+N])] += 1
            except:
                D[tuple(strparts[i:i+N])] = 1
                
        cntr = collections.Counter(D)
        spisok  = cntr.most_common(5)
        print("Output " +str(N)+"-gramms:")
        for key in spisok:
            print(str(key[0]) + " "+str(key[1]))
        
def searchNGramm(FILE):
        stringList = ''
        for line in FILE:
            words = line.split()
            requestUrl = words[6]
            username = words[7]
            part_url = ''
            try:
                part_url = re.match('(http://|.*?)(.+?|.+?\..+?)(\/|:)',requestUrl).group(2)
            except AttributeError:
                pass
            urls = part_url.split(".")
            stringList += username + urls[len(urls)-2] + "." + urls[len(urls)-1] + " "
        ngram(stringList, 3)
        ngram(stringList, 4)
        ngram(stringList, 5)

def searchRegRequest(FILE):
	dicIP = {}
	dicUser = {}
	firstTime = 0
	for line in FILE:
		words = line.split()
		if words[0] == 'time':
		    continue;
		time = int(words[0].replace('.',''))
		if firstTime == 0:
		    firstTime = time
		srcIp = words[2]
		pointTime = time-firstTime
		username = words[7]
		if username =='-':
			continue
		if username in dicUser:
			dicUser[username].append(pointTime)
		else :
			dicUser[username] = [pointTime]	
		if srcIp in dicIP:
			dicIP[srcIp].append(pointTime)
		else :
			dicIP[srcIp] = [pointTime]
	print('username')
	for user in dicUser.keys():
    		algorithmSearchSubSequence(dicUser[user], user)
	print('Ip')
	for ip in dicIP.keys():
    		algorithmSearchSubSequence(dicIP[ip], ip)
def recFunctionPopList(mas, d):
	i=0
        start = mas[0]
	print(mas)
	old = 0 
	while i<len(mas)-1:
		if start + d == mas[i+1]:
			start = mas[i+1]
			mas.pop(old)
			odl = i+1			
			print(start)
			i=0
		i +=1
def algorithmSearchSubSequence(mas,username):
	dic = {}
	i = 0
	j = 0
	while i<len(mas)-1:
		i +=1
		j = 0
		while j<i:
			#print(dic)
			if mas[i]-mas[j] in dic:
				dic[mas[i]-mas[j]].append(mas[i])
			else:
				dic[mas[i]-mas[j]] = [mas[j]]
				dic[mas[i]-mas[j]].append(mas[i])
			j +=1
	bol = False
	for val in dic.keys():
		if (len(dic[val])>3):
			bol = True
	if bol:
		print('Its similarity on frequency request from: '+username)
def requestMax(FILE):
    analize = {}
    user = []
    for line in FILE:
        words = line.split()
        time = words[0]
        responseTime = words[1]
        srcIp = words[2]
        status = words[3]
        totalRequestSize = words[4]
        requestMethod = words[5]
        requestUrl = words[6]
        username = words[7];
        if words[7]!='-':
            user.append(username)
        server = words[8]
        mimeType = words[9]
        answerSize = words[10]
        
    cntr = collections.Counter(user)
    spisok  = cntr.most_common(5)
    for key in spisok:
        print(key[0] + " "+str(key[1]))
        
def sizeMax(FILE):
    sizeList = []
    dic = {}           
    for line in FILE:
        words = line.split()
        if words[0] == 'time':
            continue 
        totalRequestSize = int(words[4])
        username = words[7]
        if username in dic:
            dic[username] = (int(dic.get(username,0)))+totalRequestSize
        else:
            dic[username]=totalRequestSize
    for i in dic:
        sizeList.append(dic[i])
    sizeList.sort(reverse=True)
    count = 0
    for i in sizeList:
        count +=1
        for name in dic:
            if (dic[name]) == (i):
                print (str(count) + " Users:"+name)
                print (':'+str(i) + "\n")
        if count == 5:
            break
#helper search Malware Url
def findUrlMalware(sLine):
    words = sLine.split()
    if len(words) == 0:
        return
    ipAdr = words[0]    
    if '#' == ipAdr or len(words)==1:
        return
    malwareSuite = words[1]
    malwareSuite2 = malwareSuite.replace("www.", "")  
    for line in FILE:
        words = line.split()
        requestUrl = words[6]
        if len(words)>11:
            referer = words[11]
        username = words[7]
        if malwareSuite in requestUrl or malwareSuite in referer or malwareSuite2 in requestUrl:
            print ("Malware host: " + malwareSuite + ". Username:"+username)
    
# task malware list in file txt
def searchMalware(FILE):    
    fileMalware = open('malw.txt','r')    
    FILE_MALW = fileMalware.readlines()
    fileMalware.close()
    for sLine in FILE_MALW:
        findUrlMalware(sLine)
        
def searchMalwareGetRequest():
    mList = []
    with urllib.request.urlopen("http://www.malwaredomainlist.com/hostslist/hosts.txt") as response:
        html = response.read()
        text = html.decode()
        sLine = text.split("\r\n")
        for line in sLine:
            findUrlMalware(line)      
    
f = open('log.txt','r')
FILE = f.readlines()
f.close()

print ('Start')
requestMax(FILE)       #task 1
sizeMax(FILE)          #task 2
searchMalware(FILE)    #task 3
searchMalwareGetRequest() #task 3
searchRegRequest(FILE) # task 4-5 
searchNGramm(FILE) #task 6
