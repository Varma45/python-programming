
def main():
    T = int(input())
    Si = [None]*T
    if T>=1 and T<=10 :
        for i in range(T) :
            Si[i] = str(input())
    for j in Si :
        print("{} {}".format(j[0:len(j):2],j[1:len(j):2]))
main()