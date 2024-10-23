

a = 0
temp_result = 2
base = 2
power = 10

while a < power-1:
    i = 1
    
    while i < base:
        temp_result += temp_result
        i += 1
    a += 1
print (temp_result)