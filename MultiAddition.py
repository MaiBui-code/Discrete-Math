##4. How many three-digit numbers contain the digits 2 and 5?
count = 0

listDigit = []
def findDigit (num):
    lastDigit = num%10
    updateNum = num//10
    secondDigit = updateNum%10
    updateNum2 = updateNum//10
    firstDigit = updateNum2%10
    listDigit.append(firstDigit)
    listDigit.append(secondDigit)
    listDigit.append(lastDigit)
    return listDigit
pickedList = []
for i in range(100,1000):
    digitList = findDigit(i)
    if (digitList[0] == 2 or digitList[1] == 2 or digitList[2] == 2) and (digitList[0] == 5 or digitList[1] == 5 or digitList[2] == 5):
        pickedList.append(i)
        count += 1
    digitList.clear()
print(pickedList)
        

print(count)


