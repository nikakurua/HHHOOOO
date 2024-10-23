n = int(input("Please enter n: "))

reversed_number = 0
k = 0
while n/10**k > 9:
    k += 1

sum_of_digits = 0

i = 0 
while i <= 9:
    if (n-i) % 10 == 0:
        reversed_number += i * 10**k
        sum_of_digits += i
        n = (n-i)/10
        k -= 1
        i = 0
    else : i += 1
    if k < 0:
        break
    
print (f"reversed number is {reversed_number}")
print(f"Sum of digits: {sum_of_digits}")


        





