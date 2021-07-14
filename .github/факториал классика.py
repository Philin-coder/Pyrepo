factorial=1
for i in range(1,4):
    for k in range(1,2*i-1):
        factorial*=k       
print("Factorial:",factorial)