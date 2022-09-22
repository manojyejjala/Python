n=int(input("Enter no of Units="))
if n<=100:
    print("No charge:")
elif n in range (150):
    print("Bill", (n-100)*4)
else:
    print("Bill", (n-150)*10)