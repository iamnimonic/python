def main():
    x = int(input("What is x?: "))
    if isEven(x):
        print('The number is even')
    else:
        print('The number is false')

def isEven(n):
    return n % 2 == 0

main()