import sys

d = int(input("Enter the degree of the polynomial d (2<=d<10) :"))
coef = []

print("enter each coefficient and press enter in the order of a0, a1 ,.... ad: ")
for i in range(d+1):
    coef.append(float(input("coefficient of x^{}:   ".format(i))))
print(coef)

def evalpoly(x) :
    f_x = 0
    for i in range(len(coef)):
        f_x = f_x + coef[i]*(x**i)
    #print(f_x)
    return f_x

def rootfinder(a,b):
   # print("c")
    m = (a+b)/2
    f_a = evalpoly(a)
    f_b = evalpoly(b)
    f_m = evalpoly(m)
    #print(f_m)
    if abs(f_m) < 10**-10:
        print("Real root is {}".format(m))
        return

    else :
        if f_a * f_m <0:
            rootfinder(a,m)
        if f_m * f_b < 0 :
            rootfinder(m,b)


def main():
    f_x_vals = []
    for x in range(0,11):
        f_x_vals.append(evalpoly(x))
        if abs(f_x_vals[x])<10**(-10):
            print("Integer root is {}".format(x))
            return

   # print(f_x_vals)

    for k in range(len(f_x_vals)):
        if f_x_vals[k]==min(f_x_vals):
            minInt = k
            break
    #print(minInt)

    for guess in range(1,len(f_x_vals)):
        if (f_x_vals[guess]*f_x_vals[guess-1])<0 :
            b = guess
            a = guess-1
           # print(a,b)
            break


    rootfinder(a,b)



main()
