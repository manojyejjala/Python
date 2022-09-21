a=int(input("Enter first value="))
b=int(input("Enter second value="))
c=int(input("Enter third value="))
if a>b and a>c:
    print("First value is greatest:",a)
elif b>c:
    print("Second value is greatest:",b)
else:
    print("Third value is greatest:",c)