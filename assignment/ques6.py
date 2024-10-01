a = [1,2,3,5,8,6,9,4,13]
largest=a[0]
smallest=a[0]

for i in a:
    if i>largest:
        largest = i
    if i<smallest:
        smallest = i

print('Smallest = ',smallest)
print('Largest = ',largest)