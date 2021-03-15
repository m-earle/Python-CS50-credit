from cs50 import get_int

def main():
    n = get_height()
    for i in range(n):
        print_space(n-i)
        print_brick(i)
        print("  ", end = "")
        print_brick(i)
        print() ##print new line after each row

def get_height():
    while True:
        n = get_int("Height:")
        if n > 0 and n < 9:
            break
    return n

def print_space(n):
    for i in range(n-1): ## w/o the -1, makes an extra space to left of pyramid
        print(" ", end = "") ##use the end thing to prevent making a new line after each space

def print_brick(n):
    for i in range(n+1):
        print("#", end = "")

main()