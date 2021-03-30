from decimal import Decimal as D , getcontext
getcontext().prec = 20100
def chud2(n):
    pi = D(13591409)
    ak = D(1)
    k = 1
    while k < n:
        ak *= -D((6*k-5)*(2*k-1)*(6*k-1))/D(k*k*k*26680*640320*640320)
        val = ak*(13591409 + 545140134*k)
        pi += val
        k += 1
    pi = pi * D(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi
    
print(str(chud2(1420))[:20002])