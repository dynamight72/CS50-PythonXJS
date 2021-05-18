n1 = 0 
n2 = 1
count = 0
#nterm = input("Please give number limit: ")
nterm = float('inf')
if nterm <= 0:
    nterm = int(input("Please give valid NUMBER limit: "))
    print(nterm)

else:
    while count < nterm:
        print(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1
