import sys
def main():
    n = int(input().strip())
    reverse = []
    position = []
    maxdiff = []
    while n!=0:
        reverse.append(int(n%2))
        n=int(n/2)

    binary = reverse[-1::-1]
    #print(binary)

    i =0
    while  i<len(binary):
        if binary[i] ==0:
            #print(i)
            position.append(i)
        i = i+1

    if len(position) == 0 :
        maxdiff.append(len(binary))
    else :

        j = 0
        while j<=len(position):
            if j == 0 :
                maxdiff.append(position[j])
            if j >0 and j<len(position):
                maxdiff.append(position[j]-position[j-1]-1)
            if j==len(position):
                maxdiff.append(len(binary)-position[j-1]-1)
            j =j+1


   # print(position)
    #print(maxdiff)
    print(max(maxdiff))




main()


