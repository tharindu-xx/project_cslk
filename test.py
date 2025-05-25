def min():
    x = int(input("Number: "))
    check(x)

def check(number):
    if number % 2 == 1:
        print("odd number")
    else:
        print("even number")
    