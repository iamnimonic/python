def main():
    meow()

def meow():
    while True:
        n = int(input('Enter a value of n: '))
        if n > 0:
            break
    for _ in range(n):
        print('meow')

main()