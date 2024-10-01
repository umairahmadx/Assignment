st='Umair Ahmad Umair Hello Hii Hello'
lst=list(st.split(" "))
dic={}
for i in lst:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i] = 1
print(dic)