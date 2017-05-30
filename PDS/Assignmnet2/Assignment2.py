import math

def dist(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("distance between these points {}".format(dist))




def main() :
    x1 = float(input("Enter Point A = (X1,Y1), X1: "))
    y1 = float(input("Enter Point A = (X1,Y1), Y1: "))
    x2 = float(input("Enter Point C = (X2 Y2), X2: "))
    y2 = float(input("Enter Point C = (X2 Y2), Y2: "))

    dist(x1,y1,x2,y2)



    if x1 == x2 :
        x3 = x1 - ((y1+y2)/2 - y1)
        y3 = (y1+y2)/2
        y4 = (y1+y2)/2
        x4 = x1 + ((y1+y2)/2 - y1)

    elif y1==y2:
        y3 = y1 - ((x1 + x2) / 2 - x1)
        x3 = (x1 + x2) / 2
        x4 = (x1 + x2) / 2
        y4 = y1 + ((x1 + x2) / 2 - x1)

    else:
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        print("Equation of the line is y = {}x+{}".format(m, c))
        cp = (y1 + y2) / 2 - (x1 + x2) / (2 * -m)
        print("Equation of other diagonal is y = {}x+{}".format(-1 / m, cp))

        m2 = -1 / m
        d1 = (x2 + x1) / 2
        d2 = (y2 + y1) / 2
        a = (1 + m2 ** 2)
        b = -2 * d1 + 2 * m2 * (cp - d2)
        d = d1 ** 2 + (cp - d2) ** 2 - ((x1 - x2) ** 2 + (y1 - y2) ** 2)/4
        print(a,b,d)
        x3 = (-b + math.sqrt((b**2) - 4 * a * d)) / (2 * a)
        x4 = (-b - math.sqrt(b** 2 - 4 * a * d)) / (2 * a)
        y3 = m2 * x3 + cp
        y4 = m2 * x4 + cp

    print(x3, y3, x4, y4)
    dist(x1, y1, x3, y3)
    dist(x1, y1, x4, y4)
    dist(x2, y2, x3, y3)
    dist(x2, y2, x4, y4)

main()

