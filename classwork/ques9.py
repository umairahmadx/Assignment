f1=open('Emp1.txt','r')
f2=open('Emp2.txt','r')
f3=open('Emp3.txt','r')

f4=open('Merge.txt','w')
f4.write(f'{f1.read()} {f2.read()} {f3.read()}')
f1.close
f2.close
f3.close
f4.close