a=int(input("Enter first value="))
b=int(input("Enter second value="))
c=int(input("Enter third value="))
d=int(input("Enter fourth value="))
if a==b or a==c or a==d or b==c or b==d or c==d:
    print("Error")
elif a>b and a>c and a>d:
    print("a is greatest")
elif b>c and b>d:
    print("b is greatest")
elif c>d:
    print ("c is greatest")
else:
    print ("d is greatest")