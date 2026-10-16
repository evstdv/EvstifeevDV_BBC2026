#task 6

import random
import os
import time

class Player:
    def __init__(self, size):
        self.exit = False
        self.hp = 100
        self.inventory = []
        self.damage = 15
        self.x = random.randint(0, size - 1)
        self.y = random.randint(0, size - 1)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def take_damage(self, damage):
        self.hp -= random.randint(abs(damage - 5), damage + 5)
        if self.hp <= 0:
            player_is_dead()
        

    def show_inventory(self):
        print('[', end = '')
        for i in range(0, len(self.inventory)):
            print(ITEM_NAMES[self.inventory[i]], end = '')
            if i != len(self.inventory) - 1:
                print(end = ', ')
        print(']')

    def pick_up(self, items):
        taken = []
        if len(items) > 1:
            print("0 - Забрать все предметы")
            for i in range(1, len(items) + 1):
                print(i, "- Забрать предмет", ITEM_NAMES[items[i - 1]])
            i += 1

            print(i, "- Оставить")
            
            choice = input("Ваш выбор: ")
            while not (choice in [str(j) for j in range(0, i + 1)] and choice):
                choice = input("Ваш выбор: ")

            #print(i, choice, choice == str(i), "choice!!!")
            
            if choice == '0':
                self.inventory.extend(items)
                taken.extend(items)
            elif choice == str(i):
                pass
            else:
                self.inventory.append(items[int(choice) - 1])
                taken.append(items[int(choice) - 1])
                #print(taken, items[int(choice) - 1], "!!!")
                    
        elif len(items) == 1:
            print("1 - Забрать предмет", ITEM_NAMES[items[0]])
            print("2 - Оставить")
            choice = input("Ваш выбор: ")
            while not (choice in "12" and choice):
                choice = input("Ваш выбор: ")
            if choice == '1':
                self.inventory.append(items[0])
                taken.append(items[0])
                
        return taken
        
class Monster:
    def __init__(self):
        self.hp = random.randint(30, 40)
        self.damage = random.randint(10, 20)
        self.alive = True
    def take_damage(self, damage):
        self.hp -= random.randint(abs(damage - 5), damage + 5)
        if self.hp <= 0:
            self.alive = False

class Chest:
    def __init__(self):
        self.is_opened = False
        self.storage = random.choices(list(ITEM_NAMES.keys()), k = random.randint(1, 3))
    def open(self):
        self.is_opened = True
    def pick_item(self, items):
        #print(items, self.storage, "???")
        for item in items:
            self.storage.remove(item)
    def show_storage(self):
        print('[', end = '')
        for i in range(0, len(self.storage)):
            print(ITEM_NAMES[self.storage[i]], end = '')
            if i != len(self.storage) - 1:
                print(end = ', ')
        print(']')

        
class Dungeon:
    def __init__(self, player_x, player_y, size):
        self.size = size

        self.visible_map = [[ICONS[HIDDEN] for _ in range(size)] for _ in range(size)]
        self.visible_map[player_x][player_y] = ICONS[PLAYER]

        self.true_map = [generate_line(size) for _ in range(size)]

        reserved_coordinates = [(player_x, player_y)]
        self.true_map[player_x][player_y] = EMPTY

        guaranted_spawn_objects = (PORTAL, KEY, KEY, CHEST, CHEST, CHEST, KEY)
        
        for obj in guaranted_spawn_objects:
            x, y = (generate_unused_coordinates(reserved_coordinates, size))
            reserved_coordinates.append((x, y))
            self.true_map[x][y] = obj

        self.entity_list = dict()
        for x in range(size):
            for y in range(size):
                if self.true_map[x][y] in ENTITIES.keys():
                    self.entity_list[(x, y)] = ENTITIES[self.true_map[x][y]]()
             
    def print_dungeon(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.visible_map[x][y], end = ' ')
            print()
                
def player_is_dead():
    print("\n\n\n\n\n\nВы умерли =(")
    exit()

def generate_unused_coordinates(reserved_coordinates, size):
    x, y = random.randint(0, size - 1), random.randint(0, size - 1)
    while (x, y) in reserved_coordinates:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
    return x, y

def generate_line(size):
    line = []
    for i in range(size):
        chance = random.randint(0, 100)
        if chance <= 35:
            line.append(EMPTY)
        elif chance <= 45:
            line.append(MONSTER)
        elif chance <= 70:
            line.append(KEY)
        elif chance <= 95:
            line.append(CHEST)
        else:
            line.append(TRAP)
    return line

def print_list_indexes(lst):
    for i in range(0, len(lst)):
        print(i + 1, "-", ITEM_NAMES[lst[i]])
        
def inventory_case_1(player, dungeon):
    print_list_indexes(player.inventory)
            
    choice = input("Ваш выбор: ")
    while not (choice in [str(i) for i in range(1, len(player.inventory) + 1)] and choice):
        choice = input("Ваш выбор: ")
    choice = int(choice) - 1
            
    chosen_item = player.inventory[choice]
            
    if chosen_item in ITEM_USE.keys():
        player.inventory.remove(chosen_item)
        ITEM_USE[chosen_item](player, dungeon)
    else:
        print("Вы не можете использовать", ITEM_NAMES[chosen_item])

def inventory_case_2(player, dungeon):
    print_list_indexes(player.inventory)
            
    choice = input("Ваш выбор: ")
    while not (choice in [str(i) for i in range(1, len(player.inventory) + 1)] and choice):
        choice = input("Ваш выбор: ")
    choice = int(choice) - 1
    
    chosen_item = player.inventory[choice]
            
    new_name = input("Введите новое название для предметов этого типа: ")
    ITEM_NAMES[chosen_item] = new_name
    
    

def inventory_case_3(player, dungeon):
    print_list_indexes(player.inventory)
            
    choice = input("Ваш выбор: ")
    while not (choice in [str(i) for i in range(1, len(player.inventory) + 1)] and choice):
        choice = input("Ваш выбор: ")
    choice = int(choice) - 1
            
    chosen_item = player.inventory[choice]
            
    player.inventory.remove(chosen_item)

def inventory_playing(player, dungeon):
    if len(player.inventory) == 0:
        print("Вы не можете сделать что-то с пустым инвентарём")
        return
    
    print("\n1 - Использовать предмет из инвентаря")
    print("2 - Переименовать предмет из инвентаря")
    print("3 - Выкинуть предмет из инвентаря")
    print("4 - Сортировать инвентарь")
    print("5 - Перевернуть инвентарь")
    print("6 - Ничего не делать")

    choice = input("Ваш выбор: ")
    while not (choice in "123456" and choice):
        choice = input("Ваш выбор: ")
    
    match choice:
        case '1':
            inventory_case_1(player, dungeon)
        case '2':
            inventory_case_2(player, dungeon)
        case '3':
            inventory_case_3(player, dungeon)
        case '4':
            player.inventory.sort()
        case '5':
            player.inventory.reverse()
        case _:
            pass
            
            

def click_analysis(key, player, dungeon):
    key = key.lower()
    match key:
        case 'i':
            print("Вот ваш инвентарь:")
            player.show_inventory()
            inventory_playing(player, dungeon)
        case 'w':
            step_processing(0, -1, player, dungeon)
        case 'a':
            step_processing(-1, 0, player, dungeon)
        case 's':
            step_processing(0, 1,  player, dungeon)
        case 'd':
            step_processing(1, 0,  player, dungeon)
        case _:
            print("Вы не попали по кнопке =(")
            
def step_processing(dx, dy,  player, dungeon):
    if player.x + dx >= dungeon.size or player.y + dy >= dungeon.size:
        return None
    if player.x + dx < 0 or player.y + dy < 0:
        return None

    dungeon.visible_map[player.x][player.y] = ICONS[dungeon.true_map[player.x][player.y]]
    player.move(dx, dy)
    dungeon.visible_map[player.x][player.y] = ICONS[PLAYER]

    dungeon.print_dungeon()

    print()
    PLAY_EVENT[dungeon.true_map[player.x][player.y]](player, dungeon)

def event_empty(player, dungeon):
    print("Здесь пусто")

def event_key(player, dungeon):
    print("Вы нашли ключ!")
    print("\nВаш инвентарь выглядит так:")
    player.show_inventory()
    
    player.pick_up((ITEM_KEY,))
    dungeon.true_map[player.x][player.y] = EMPTY


def event_monster(player, dungeon):
    print("Вы встретили монстра!")
    monster = dungeon.entity_list[(player.x, player.y)]
    print("Ваши hp -", player.hp, ",hp монстра -", monster.hp)
    
    print("1 - Сражаться")
    print("2 - Пытаться бежать")
    
    choice = input("Ваш выбор: ")
    while not (choice in "12" and choice):
        choice = input("Ваш выбор: ")
    if choice == '1':
        fight(player, monster)
    if choice == '2':
        if random.randint(0, 1) == 0:
            print("Не вышло. Монстр больно ударил вас в спину")
            player.take_damage(30)
            fight(player, monster)
        else:
            print("Вы сбежали")
    if not monster.alive:
        dungeon.true_map[player.x][player.y] = EMPTY
    

def fight(player, monster):
    while monster.alive:
        player.take_damage(monster.damage)
        monster.take_damage(player.damage)
        print("Ваши hp -", player.hp, ",hp монстра -", monster.hp)
        time.sleep(0.3)
    print("Монстр умер.")
    
def event_trap(player, dungeon):
    print("Вы попались в ловушку...")
    player.take_damage(16)
    print("Ваши hp -", player.hp)
    

def event_portal(player, dungeon):
    print("Вы увидели портал!\n")
    print("1 - Выйти")
    print("2 - Остаться")
    choice = input("Ваш выбор: ")
    while not (choice in "12" and choice):
        choice = input("Ваш выбор: ")
    if choice == '1':
        player.exit = True

def event_chest(player, dungeon):
    print("Перед вами сундук!\n")
    chest = dungeon.entity_list[(player.x, player.y)]
    if not chest.is_opened:
        if ITEM_KEY in player.inventory:
            print("1 - Уйти")
            print("2 - Применить предмет Ключ")
            
            choice = input("Ваш выбор: ")
            while not (choice in "12" and choice):
                choice = input("Ваш выбор: ")
                
            if choice == '2':
                chest.open()
                player.inventory.remove(ITEM_KEY)
        else:
            print("Но что вы с ним сделаете?..")
                
    if chest.is_opened:
        print("\nВаш инвентарь:")
        player.show_inventory()
        print("\nВот содержимое сундука:")
        chest.show_storage()
        chest.pick_item(player.pick_up(chest.storage))

def use_map(player, dungeon):
    print("Вы посмотрели на старую карту")
    for _ in range(size):
        x, y = random.randint(0, dungeon.size - 1), random.randint(0, dungeon.size - 1)
        dungeon.hidden_map[x][y] = dungeon.true_map[x][y]
        
def use_sword(player, dungeon):
    print("Ваш урон увеличен")
    player.damage += 5
    
def use_potion(player, dungeon):                
    print("Ваши hp восстановлены")
    player.hp += 50
        
    
            
def main():
    size = 8
    player  = Player(size)
    dungeon = Dungeon(player.x, player.y, size)

    dungeon.print_dungeon()

    print("\nИспользуйте WASD для перемещения по карте, I для взаимодействия с инвентарём")
    
    while True:
        if player.exit == True:
            player.exit = False
            print("\nВы на новом этаже.")
            
            dungeon = Dungeon(player.x, player.y, size)
            dungeon.print_dungeon()
            
        key = input("\nВаш следующий шаг: ")
        click_analysis(key, player, dungeon)

        
ITEM_KEY, ITEM_HP, ITEM_MAP, ITEM_BROKEN_SWORD, ITEM_SEE_PORTAL, ITEM_SOMETHING_1 = range(6)

ITEM_NAMES = {ITEM_KEY : "Ключ", ITEM_MAP : "Карта",
              ITEM_BROKEN_SWORD : "Меч", ITEM_SEE_PORTAL : "Хлам",
              ITEM_HP : "Зелье", ITEM_SOMETHING_1 : "Мусор"}

ITEM_USE   = {ITEM_MAP : use_map,
              ITEM_BROKEN_SWORD : use_sword,
              ITEM_HP : use_potion}

MONSTER, KEY, CHEST, TRAP, PORTAL, HIDDEN, EMPTY, PLAYER = range(8)

ENTITIES = {MONSTER : Monster, CHEST : Chest}

ICONS =  {MONSTER : 'M', KEY : 'K', CHEST : 'C', TRAP : 'T', PORTAL : 'P', HIDDEN : '■', EMPTY : '□', PLAYER : '@'}

PLAY_EVENT = {MONSTER : event_monster, KEY : event_key,
          CHEST : event_chest, TRAP : event_trap,
          PORTAL : event_portal, EMPTY : event_empty}

main()
