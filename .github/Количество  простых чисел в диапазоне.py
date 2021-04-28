def isprime(n):
    from math import log, sqrt
 
    def is_prime(i):
        m = min(i, int(sqrt(p_limit_n)))
        l = range(2, m)
        r = map(lambda x: i % x == 0, l)
        return not any(r)
 
    p_limit_n = int((log(n) + log(log(n)) - 0.5)*n) + 10
    ls = range(2, p_limit_n)
    
    ls2 = list(filter(is_prime, ls))
    print(*ls2[:n])
 
 
if __name__ == '__main__':
    n = 10
    if n == 1:
        print(2)
    else:
        isprime(n)