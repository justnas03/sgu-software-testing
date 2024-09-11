import math

#printd = print
printd = lambda *argc,**argv:()



def giaiptb2(a,b,c):
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
            x1 = (-b-math.sqrt(delta))/2*a
            x2 = (-b+math.sqrt(delta))/2*a
            if x1 > x2: x1, x2 = x2, x1
            
    return x1,x2,sn

printd(giaiptb2(1,0,1))

def main():
    
    s = input("")
    a,b,c = [float(x) for x in s.split(" ")]

    x1,x2,sn = giaiptb2(a,b,c)

    if sn == -1:
        print(f"Phương trình vô nghiệm")
    elif sn == 0:
        print(f"Phương trình vô nghiệm")
    elif sn == 1:
        print(f"Phương trình có 1 nghiệm: x = {x1}")
    elif sn == 2:
        print(f"Phương trình có 2 nghiệm: x1 = {x1}, x2 = {x2}")


if __name__ == "__main__":
    main()
