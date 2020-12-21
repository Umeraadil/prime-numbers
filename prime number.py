print("CODE BY UMER AADIL")
print("FIND A NUMBER IS PRIME OR NOT")
def is_prime(num):
   for i in range(2,num):
       if (num % i) == 0:
           return False
   return True


num = int(input("Enter a number: "))

check = prime(num)

if check:
   print('Number is a Prime')
else:
   print('Number is not a Prime')