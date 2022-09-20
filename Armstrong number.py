num = int(input("Enter a number:"))

def check_armstrong(num):

    order = len(str(num))
    sum = 0
    
    while num>0:
      digit = num % 10
	  sum += digit ** order
      num = num // 10
	
    if sum == original:
        return True
    return False
    
if check_armstrong(number):
    print('number is armstrong')
else:
    print('number is not armstrong')