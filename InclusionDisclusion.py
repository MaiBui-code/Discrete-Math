##How many integers between 1 and 500 are divisible by 3 but not by 5 or 6?
count = 0
number = []
for i in range (500):
    if i % 3 == 0 and (i%5 != 0 and i%6 != 0):
        number.append(i)
        count += 1
    else:
        count += 0

print(count)
print (number)
print(len(number))


