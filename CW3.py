element = 999
myNumbers = []
while(element != 0):
    element = int(input("Elements up to zero: "))
    myNumbers.append(element)
del myNumbers[-1]
index = int(input("Enter the index: "))
myNumbers2 = []
for i in myNumbers:
    if (i < myNumbers[index]):
        myNumbers2.append(i)
print("The array: ",myNumbers)
maxi = 0
for i in myNumbers2:
    if (i > maxi):
        maxi = i
if (maxi == 0):
    maxi = -1
print("The searched element: ",maxi)
