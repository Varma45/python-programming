import sys

def main():
    n = int(input().strip())

    phoneBook = dict()
    for i in range(n):
        perlineData = input().split(' ')
        phoneBook[perlineData[0]] = perlineData[1]

    for j in range(n):
        x = input()
        if x in phoneBook :
            print(x,'=',phoneBook.get(x),sep='')
        else:
            print('Not found')

main()