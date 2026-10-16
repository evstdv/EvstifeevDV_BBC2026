class Calculator:
    def __init__(self, operations, transform_arg):
        self.operations = operations
        self.transform_arg = transform_arg
    
    def calculate(self, first_arg, operator, second_arg):
        operation = self.operations.get(operator)

        if operation == None:
            return f"Ошибка: в калькуляторе не существует оператора '{operator}'"
        else:
            try:
                first_arg = self.transform_arg(first_arg)
            except:
                return f"Ошибка: в калькуляторе не существует аргумента '{first_arg}'"
            
            try:
                second_arg = self.transform_arg(second_arg)
            except:
                return f"Ошибка: в калькуляторе не существует аргумента '{second_arg}'"
            
            try:
                result = operation(first_arg, second_arg)
            except:
                return f"Ошибка: оператор '{operator}' неприменим для аргументов '{first_arg}' и '{second_arg}'"
            
            return f"Результат: {result}"
        
def choose_calc():
    print("1 - DEC")
    print("2 - BIN")
    print("3 - OCT")
    print("4 - HEX")
    print("5 - COD")

    chosen_num = int(input("Введите номер калькулятора: "))
    print()
    
    match chosen_num:
        case 1:
            return decimal_calculator
        case 2:
            return binary_calculator
        case 3:
            return octal_calculator
        case 4:
            return hex_calculator
        case 5:
            return shiz_calculator
        case _:
            print("Выбранного калькулятора не существует. Текущий калькулятор - DEC", end = "\n\n")
            return decimal_calculator


def plus(first_arg, second_arg):
    return first_arg + second_arg

def minus(first_arg, second_arg):
    return first_arg - second_arg

def multiply(first_arg, second_arg):
    return first_arg * second_arg

def divide(first_arg, second_arg):
    return first_arg / second_arg

def powpow(first_arg, second_arg):
    return first_arg ** second_arg


def transform_dec(arg):
    return int(arg, 10)

def transform_bin(arg):
    return int(arg, 2)

def transform_oct(arg):
    return int(arg, 8)

def transform_hex(arg):
    return int(arg, 16)

def transform_shz(arg):
    return ord(arg)

def input_expression():
    first_arg = input("Введите аргумент: ")
    if first_arg == "opt" or first_arg == "'opt'":
        return "opt", None, None
    
    operator = input("Введите оператор: ")
    if operator == "opt" or operator == "'opt'":
        return "opt", None, None

    second_arg = input("Введите аргумент: ")
    if second_arg == "opt" or second_arg == "'opt'":
        return "opt", None, None

    return first_arg, operator, second_arg

math_operations = {"+" : plus,
                   "-" : minus,
                   "*" : multiply,
                   "/" : divide,
                   "^" : powpow}

shiz_operations = {"ы":     plus,
                   "авава": multiply}

decimal_calculator = Calculator(math_operations, transform_dec)
binary_calculator  = Calculator(math_operations, transform_bin)
octal_calculator   = Calculator(math_operations, transform_oct)
hex_calculator     = Calculator(math_operations, transform_hex)
shiz_calculator    = Calculator(shiz_operations, transform_shz)

current_calculator = decimal_calculator

print("Для вызова меню смены калькулятора передайте в качестве аргумента 'opt'")
print("=======================================================================")

while True:
    first_arg, operator, second_arg = input_expression()
    
    if first_arg == "opt":
        current_calculator = choose_calc()
    else:
        print(current_calculator.calculate(first_arg, operator, second_arg), end = "\n\n")

