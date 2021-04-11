def test(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return i
    return n
 
if __name__ == '__main__':
    print(test(n=12))