class Level:
    def __init__(self, description, game, take_arguments):
        self.description = description
        self.game = game
        self.take_arguments = take_arguments
        
    def show_description(self):
        for line in self.description:
            print(line)
        print()
 
    def take_all_for_game(self):
        method_num = int(input("Введите номер метода: "))
        arguments = self.take_arguments(method_num)
        print()
        return (method_num, arguments)
            
    def play_game(self, method_num, arguments):
        self.game(method_num, arguments)
        
 
def choose_level_num():
    level_num = int(input("Введите номер уровня: "))
    print()
    return level_num
 
def take_arguments_1(method_num):
    arguments = []
    arguments.append(input("Введите строку: "))
 
    return arguments
 
def take_arguments_2(method_num):
    arguments = []
    arguments.append(input("Введите строку: "))
 
    if method_num == 1:
        arguments.append(input("Введите слово для поиска: "))
    elif method_num == 2:
        arguments.append(input("Введите заменяемое слово: "))
        arguments.append(input("Введите заменяющее слово: "))
    elif method_num == 3:
        arguments.append(input("Введите слово для поиска: "))
 
    return arguments
 
def take_arguments_3(method_num):
    arguments = []
    arguments.append(input("Введите строку: "))
 
    if method_num == 1:
        arguments.append(input("Введите слово для поиска: "))
    elif method_num == 2:
        arguments.append(input("Введите заменяемое слово: "))
        arguments.append(input("Введите заменяющее слово: "))
    elif method_num == 3:
        arguments.append(input("Введите слово для поиска: "))
 
    return arguments
 
def take_arguments_4(method_num):
    arguments = []
    arguments.append(input("Введите строку: "))
 
    return arguments
 
def take_arguments_5(method_num):
    arguments = []
    arguments.append(input("Введите строку: "))
 
    return arguments
 
def game_1(method_num, arguments):
    string: str = arguments[0]
    
    if method_num == 1:
        print(string.upper())
    elif method_num == 2:
        print(string.lower())
    elif method_num == 3:
        print(string.capitalize())
 
def game_2(method_num, arguments):
    string = arguments[0]
    if method_num == 1:
        print(string.find(arguments[1]))
    elif method_num == 2:
        string = string.replace(arguments[1], arguments[2])
        print(string)
    elif method_num == 3:
        print(string.count(arguments[1]))
            
def game_3(method_num, arguments):
    string = arguments[0]
    if method_num == 1:
     print(string.split(arguments[1]))
    elif method_num == 2:
     string = string.split(arguments[1])
     print(arguments[2].join(string))
 
def game_4(method_num, arguments):
    string = arguments[0]
    if method_num == 1:
     print(string.isdigit())
    elif method_num == 2:
     print(string.isalpha())
 
def game_5(method_num, arguments):
    print("~~ Python is awesome ~~")   
 
def fill_level_list():
    level_list = []
    
    description_1 = ("Реализовано 3 метода:",
                            "1: Возвращает копию строки со всеми символами, преобразованными в верхний регистр",
                            "2: Возвращает копию строки со всеми символами, преобразованными в нижний регистр",
                            "3: Возвращает копию строки с первым символом, преобразованным в верхний регистр")
    
    description_2 = ("Реализовано 3 метода:",
                            "1: Найти первую позицию выбранного слова",
                            "2: Заменить все вхождения выбранного слова на другое выбранное слово",
                            "3: Вернуть количество выбранного слова в строке")
 
    description_3 = ("Реализовано 2 метода:",
                            "1: Вернуть строку, разделённую по выбранному разделителю. split()",
                            "2: Заменить все вхождения выбранного слова на другое выбранное слово. split() + join()")
 
    description_4 = ("Реализовано 2 метода:", "1: Проверить, является ли строка числом", "2: Проверить, является ли строка словом только из алфавитных букв")
 
    description_5 = ("( ͡° ͜ʖ ͡°)",)
 
    level_list.append(Level(description_1, game_1, take_arguments_1))
    level_list.append(Level(description_2, game_2, take_arguments_2))
    level_list.append(Level(description_3, game_3, take_arguments_3))
    level_list.append(Level(description_4, game_4, take_arguments_4))
    level_list.append(Level(description_5, game_5, take_arguments_5))
 
    return level_list
    
def main():
    level_list = fill_level_list()
    while True:
        level_num = choose_level_num()
        current_level = level_list[level_num - 1]
        
        current_level.show_description()
        all_for_game = current_level.take_all_for_game()
        current_level.play_game(*all_for_game)
 
        print()
        print("~" * 60, end = "\n\n")
 

main()
