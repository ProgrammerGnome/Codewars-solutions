This time no story, no theory. The examples below show you how to write function accum:

Examples: accum("abcd") -> "A-Bb-Ccc-Dddd"; accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"; accum("cwAt") -> "C-Ww-Aaa-Tttt" 
The parameter of accum is a string which includes only letters from a..z and A..Z.

```python
def accum(s):
 m=len(s)+1
 u=""
 for i,n in enumerate(s):
   u+=n.upper()+n*i+"-"
 result=u
 return result[:-1]
string = input("Enter a string: ");
print (accum(string))
```
