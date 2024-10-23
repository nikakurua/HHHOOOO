n = int(input("Please enter n: "))
k = 0
while k <= n:
    print(2*(n-k)*" ",sep = "",end = " ")
    
    i = k
    while i >= 0:
        print (i,end = " ")
        i -= 1
    
    i += 2
    
    while i <= k:
        print(i,end = " ")
        i += 1
    k += 1
    print("",end = "\n")
    
    

    



