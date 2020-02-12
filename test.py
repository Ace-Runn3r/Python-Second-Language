L = [1,2,3,4,5,6,7,8,9,0,5,4,5,5,6,4,3,5,7,8,5,5,5,5,6]

for item in L:
    print(item)
    if item is 5:
        L.remove(item)
        print(L)
print(L)