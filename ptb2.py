def ptb2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình vô số nghiệm")
            else:
                print("Phương trình vô nghiệm")
        else:
            print("Phương trình có nghiệm x = {:.4f}".format(-c/b))
    if a != 0:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm")
        elif delta == 0:
            print("Phương trình có nghiệm kép x = {:.4f}".format(-b/(2*a)))
        else:
            print("Phương trình có 2 nghiệm phân biệt x1 = {:.4f} và x2 = {:.4f}".format((-b + delta**0.5)/(2*a), (-b - delta**0.5)/(2*a)))


def main():
    s = input()
    a,b,c = [float(x) for x in s.split(" ")]
    ptb2(a,b,c)


main()


