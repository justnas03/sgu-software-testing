from ptb2 import ptb2

def pttrungphuong(a, b, c):
    if a == 0:
        print(f"Do a=0 nên phương trình quy về phương trình bậc 2.\n")
        ptb2(b, c, 0)
        return
    else:
        # đặt t tính delta
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm")
        elif delta == 0:
            t = -b / (2*a)
            if t < 0:
                print("Phương trình vô nghiệm")
            elif t == 0:
                print("Phương trình có nghiệm x = 0")
            else:
                print("Phương trình có hai nghiệm x1 = {:.4f} và x2 = {:.4f}".format(t**0.5, -(t**0.5)))
        else:
            #tính nghiệm t1, t2
            t1 = (-b + delta**0.5) / (2*a)
            t2 = (-b - delta**0.5) / (2*a)
            
            nghiem = []
            if t1 > 0:
                nghiem.append(t1**0.5)
                nghiem.append(-(t1**0.5))
            elif t1 == 0:
                nghiem.append(0)
            if t2 > 0:
                nghiem.append(t2**0.5)
                nghiem.append(-(t2**0.5))
            elif t2 == 0:
                nghiem.append(0)

            if len(nghiem) == 0:
                print("Phương trình vô nghiệm")
            elif len(nghiem) == 1:
                print("Phương trình có nghiệm x = {:.4f}".format(nghiem[0]))
            elif len(nghiem) == 2:
                print("Phương trình có hai nghiệm x1 = {:.4f} và x2 = {:.4f}".format(nghiem[0], nghiem[1]))
            else:
                print("Phương trình có bốn nghiệm x1 = {:.4f}, x2 = {:.4f}, x3 = {:.4f} và x4 = {:.4f}".format(nghiem[0], nghiem[1], nghiem[2], nghiem[3]))

def main():
    pttrungphuong(1, -6, 8)

if __name__ == "__main__":
    main()
