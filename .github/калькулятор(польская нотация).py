def rpn(a):
    s=[]
    for x in a:
        if (x == '+'):
            a2=s[0]
            a1=s[1]
            r=int(a1)+int(a2)
            s=[r]+s[2:]
        elif (x == '-'):
            a2=s[0]
            a1=s[1]
            r=int(a1)-int(a2)
            s=[r]+s[2:]
        elif (x == '*'):
            a2=s[0]
            a1=s[1]
            r=int(a1)*int(a2)
            s=[r]+s[2:]
        elif (x == '/'):
            a2=s[0]
            a1=s[1]
            r=int(a1)//int(a2)
            s=[r]+s[2:]
        else:
            s=[x]+s
    return s[0]
 
aa=input()
res=rpn(aa.split())
print(res)