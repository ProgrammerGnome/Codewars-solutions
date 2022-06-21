def accum(s):
 m=len(s)+1
 u=""
 for i,n in enumerate(s):
   u+=n.upper()+n*i+"-"
 result=u
 return result[:-1]
string = input("Enter a string: ");
print (accum(string))
