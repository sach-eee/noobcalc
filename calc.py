def add (a,b) :
    calc = a + b
    return (calc)
def subs (a,b) :
    calc = a - b
    return calc
def mul (a,b) :
    calc = a * b
    return calc
def divi (a,b) :
    calc = a/b
    return calc

def run() :
    print (" Select operation. \n 1.Add \n 2.Substract \n 3.Multiply \n 4.divide ")

    choice = int (input (" Enter chice (1/2/3/4) "))

    if choice == 1 :
        a = int (input (" Enter first number: "))
        b = int (input (" Enter second number : "))
        print(add(a,b))
    elif choice == 2 :
        a = int (input (" Enter first number: "))
        b = int (input (" Enter second number : "))
        print(subs(a,b))
    elif choice == 3 :
        a = int (input (" Enter first number: "))
        b = int (input (" Enter second number : "))
        print(mul(a,b))
    elif choice == 4 :
        a = int (input (" Enter first number: "))
        b = int (input (" Enter second number : "))
        print(divi(a,b))
    else:
        print (" You entered a wrong input ")
        run()



run()
