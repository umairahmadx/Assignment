f=open('vowel.txt','r')
s=f.read()
vowel='aeiou'
di={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in s:
    if i.lower() in vowel:
        di[i.lower()]+=1
print(di)