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
        print("Выводим " +str(N)+"-граммы:")
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

    f = open('log.txt','r')
    FILE = f.readlines()
    f.close()
    print ('Start')
    searchNGramm(FILE)