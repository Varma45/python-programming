import math

def dist(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("distance between these points {}".format(dist))




def main() :
    x1 = float(input("Enter Points P = (X1,Y1), X1: "))
    y1 = float(input("Enter Points P = (X1,Y1), Y1: "))
    x2 = float(input("Enter Points Q = X2 Y2, X1: "))
    y2 = float(input("Enter Points Q = X2 Y2, y1: "))

    dist(x1,y1,x2,y2)
    m = (y2-y1)/(x2-x1)
    c = y1-m*x1
    print("Equation of the line is y = {}x+{}".format(m,c))
    cp = (y1+y2)/2-(x1+x2)/(2*-m)
    print("Equation of Perpendicular bisector is y = {}x+{}".format(-1/m,cp))

    a = (1+(-1/m)**2)
    b = -2*x1+2*(-1/m)*(cp-y1)
    d = (x1**2)+cp**2+y1**2-2*cp*y1-((x2-x1)**2+(y2-y1)**2)

    x3 = (-b+math.sqrt(b*b-4*a*d))/(2*a)
    x4 = (-b - math.sqrt(b * b - 4 * a * d)) / (2 * a)
    y3 = (-1/m)*x3+cp
    y4 = (-1/m)*x4 + cp
    print(x3,y3,x4,y4)
    dist(x1,y1,x3,y3)




main()
