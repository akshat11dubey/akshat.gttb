a="Hello python and ml"
words=a.split()
dic={}
for i in a:
    if(i[0] not in dic.keys()):
        dic[i[0]].append(i)
    else:
        
