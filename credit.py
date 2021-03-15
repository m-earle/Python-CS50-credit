from cs50 import get_int

number = get_int("Number:")
digits = []
checksum = 0
n = 0
##print(f"{number}")
if number >= 1000000000000000 and number < 10000000000000000:
    n = 16
if number >= 100000000000000 and number < 1000000000000000:
    n = 15
if number >= 1000000000000 and number < 10000000000000:
    n = 13
if n != 16 and n != 15 and n != 13:
    print("INVALID")
else:
    for i in range(n):
        digits.append(number % 10)
        number = (number - digits[i])/ 10
    ##for i in range(n):
        ##print(f"{digits[i]}")
    for i in range(1,len(digits),2):
        if (digits[i] * 2) > 9:
            checksum = checksum + 1 + ((digits[i] * 2) % 10)
        else:
            checksum = checksum + (digits[i] * 2)
    for i in range(0,len(digits),2):
        checksum = checksum + digits[i]
    ##print(f"{checksum}")
    if checksum % 10 != 0:
        print("INVALID")
    elif len(digits) == 15 and digits[len(digits)-1] == 3:
        if digits[len(digits)-2] == 4 or digits[len(digits)-2] ==7:
            print("AMEX")
    elif len(digits) == 16:
        if digits[len(digits)-1] == 5 and digits[len(digits)-2] > 0 and digits[len(digits)-2] < 6:
            print("MASTERCARD")
        elif digits[len(digits)-1] == 4:
            print("VISA")
    elif len(digits) == 13 and digits[len(digits)-1] == 4:
        print("VISA")
    else:
        print("INVALID")
