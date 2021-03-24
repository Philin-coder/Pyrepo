n=int(input("n="))
k=int(input("k="))
if n & (1<<k):
    print(1)
else:
    print(0)