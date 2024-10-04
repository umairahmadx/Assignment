lst = [1,2,3,5,8,6,9,4,13,6]
largest=lst[0]
smallest=lst[0]

for i in lst:
    if i>largest:
        largest = i
    if i<smallest:
        smallest = i

print('Smallest = ',smallest)
print('Largest = ',largest)