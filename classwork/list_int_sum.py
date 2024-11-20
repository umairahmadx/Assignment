def sumIntList(hetroList):
    sumInt=0
    concatStr=""
    for i in hetroList:
        if type(i) == int:
            sumInt+=i
        elif type(i) == str:
            concatStr+=i
    print(sumInt)
    print(concatStr)

l1=['xyz',1,2,3,4.5,1,10.66,'uma']
sumIntList(l1)