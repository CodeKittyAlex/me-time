
def pluss(a,b):
    return a+b

def minus(a,b):
    return a-b

def add(a,b):
    return a*b

def sub(a,b):
    if b != 0:
        return a/b
    else:
        return "error!"

def calc():
    print("Select operation:")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")

    while True:
        choice = input("enter choice (1/2/3/4)")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number"))
                num2 = float(input("enter second number"))

                if choice == '1':
                    print(f"{num1} + {num2} = {pluss(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {minus(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {add(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {sub(num1, num2)}")
            except ValueError:
                print("invalid input! please try again")
        else:
            print("invalid choice! plese try  again")

            next_calculation = input("do you wanna go again?")
            if next_calculation.lower() != 'yes':
                break

if __name__ == "__main__":
    calc()

