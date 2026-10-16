def plus(first_arg, second_arg):
    return first_arg + second_arg

def minus(first_arg, second_arg):
    return first_arg - second_arg

def multiply(first_arg, second_arg):
    return first_arg * second_arg

def divide(first_arg, second_arg):
    return first_arg / second_arg

def calc(a, o, b):
    if o == '+':
        print(plus(a, b))
        
    if o == '-':
        print(minus(a, b))
        
    if o == '/':
        print(divide(a, b))
        
    if o == '*':
        print(multiply(a, b))
while True:
    a = int(input("Введите аргумент: "))
    o = input("Введите оператор: ")
    b = int(input("Введите аргумент: "))

    print("Результат: ", end = "")
    calc(a, o, b)


