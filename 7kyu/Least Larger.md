Task: Given an array of numbers and an index, return either the index of the smallest number that is larger than the element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ). (7 kyu)

Notes

Multiple correct answers may be possible. In this case, return any one of them. The given index will be inside the given array. The given array will, therefore, never be empty.

Example
```
least_larger({4, 1, 3, 5, 6}, 5, 0) == 3
least_larger({4, 1, 3, 5, 6}, 5, 4) == -1;
```
```python
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
```
