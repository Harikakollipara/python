a=int(input())
b=int(input())
c=int(input())
print("The smallest of 3 numbers:")
if(a<b and a<c):
    print(a)
elif(b<a and b<c):
    print(b)
elif(c<a and c<b):
    print(c)
elif(a==b==c):
    print("all are same")
elif(a==b and b<c):
    print(b)
elif(a>b and b==c):
     print(b)
