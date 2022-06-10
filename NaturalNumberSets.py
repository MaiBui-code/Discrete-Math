# list of numbers: F = [(1,1), (1,2), (2,1), (1,3), (2,2), (3,1), ...]
# we want to devide the list into small sets of numbers, each with different sum: S =2, 3,4
# input: number n indicate the index of F: 2
# output: number at that index (1,2)

#initiate F as an empty list
F = []
#initiate the sum
sum = 2
a = 1
b = 1
for sum in range (2,20):
    #for each sum: ex: sum = 3: add 2 elements: (1,2), (2,1)
    while a < sum :
        b = sum - a
        F.append((a,b))
        #update a
        a = a + 1 
    a = 1
print(F[65])
#print(F)

#from the value (6,6) give out the index
# = F.index((7,1))
#print(index)