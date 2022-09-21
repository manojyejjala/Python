card_valid=input("Insert the card?")
if card_valid=="yes":
    pin=int(input("Enter Pin:"))
    if pin==1234:
        amount=int(input("Enter Amount="))
        if amount<=1500 and amount%100==0:
            print("Please collect your amount")
        else:
            print("Invalid amount")
    else:
        print("Invalid pin")
else:
    print("Invalid card")