
# printd = print
printd = lambda *argc,**argv:()

def giaiptb2(a,b,c):
    import math
    x1,x2,sn = None, None, None
    if a == 0: 
        if b == 0:
            if c == 0:
                sn = -1
            else:
                sn = 0
        else: 
            sn = 1
            x1 = -c/b
    else: 
        delta = b**2 - 4*a*c
        if delta < 0:
            sn = 0
        elif delta == 0:
            sn = 1
            x1 = -b/2*a
        elif delta > 0:
            sn = 2
            x1 = (-b+math.sqrt(delta))/2*a
            x2 = (-b-math.sqrt(delta))/2*a
            if x1 > x2: x1, x2 = x2, x1
    return x1,x2,sn



def pttp(a,b,c):
    import math
    sn,x1,x2,x3,x4 = None, None, None, None, None


    t1,t2,snt = giaiptb2(a,b,c)
    printd(t1,t2,snt)

    if snt == -1:
        sn = -1
    elif snt == 0:
        sn = 0
    elif snt == 1:
        if t1 < 0:
            sn = 0
        elif t1 == 0:
            sn = 1
            x1 = 0
        elif t1 > 0:
            sn = 2
            x1 = -math.sqrt(t1)
            x2 = math.sqrt(t1)
    elif snt == 1:
        if t2 < 0:
            sn = 0
        elif t2 == 0:
            sn = 1
            x1 = 0
        elif t2 > 0:
            sn = 2
            x1 = -math.sqrt(t2)
            x2 = math.sqrt(t2)
    elif snt == 2:
        if t1 < 0:
            sn == 2
            x1 = -math.sqrt(t2)
            x2 = math.sqrt(t2)
        elif t2 < 0:
             sn == 2
             x1 = -math.sqrt(t1)
             x2 = math.sqrt(t1)
    elif snt == 2:
        if t1 == 0:
            sn = 3
            x1 = 0
            x2 = -math.sqrt(t2)
            x3 = math.sqrt(t2)
        elif t2 == 0:
            sn = 3
            x1 = 0
            x2 = -math.sqrt(t1)
            x3 = math.sqrt(t1)       
    elif snt == 2:
        if t1 > 0 and t2 > 0:
            sn = 4
            x1 = -math.sqrt(t1)
            x2 = math.sqrt(t1)
            x3 = -math.sqrt(t2)
            x4 = math.sqrt(t2)
    return sn,x1,x2,x3,x4

def main():
    s = input()
    printd(s.split(" "))
    a,b,c = [float(i) for i in s.split(" ") ]
    printd(a,b,c)

    sn,x1,x2,x3,x4 = pttp(a,b,c)
    printd(sn, x1,x2,x3,x4)

    if sn == -1:
        print(f"Phương trình vô số nghiệm")
    elif sn == 0:
        print(f"Phương trình vô nghiệm")
    elif sn == 1:
        print(f"Phương trình có 1 nghiệm x = {x1}")
    elif sn == 2:
        print(f"Phương trình có 2 nghiệm x1 = {x1}; x2 = {x2}")
    elif sn == 3:
        print(f"Phương trình có 3 nghiệm x1 = {x1}; x2 = {x2}; x3 = {x3}")
    elif sn == 4:
        print(f"Phương trình có 4 nghiệm x1 = {x1}; x2 = {x2}; x3 = {x3}; x4 = {x4}")

if __name__ == "__main__":
    main()
