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
f = open('log.txt','r')
FILE = f.readlines()
f.close()
print ('Start')
searchRegRequest(FILE)
#mas = [1,2, 8, 9, 11, 15, 18, 22] #testing param 1 8 15 22 (0,2,5,7)
#recFunctionPopList(mas,7)
