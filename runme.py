from bank import bank
from simple_term_menu import TerminalMenu

TITLE = "ELEVATOR SIMULATOR by Brian L. Gentry"

def show_title():
    print(TITLE)
    print()

def teleport():
    el = select_car()
    fl = select_floor()
    b.cars[el].location = fl

def toggle_doors():
    num = select_car()
    if (b.cars[num].doors_open == 0):
        b.cars[num].doors_open = 1
    else:
        b.cars[num].doors_open = 0

def press_button():
    car = select_car()
    floor = select_floor()
    b.cars[car].press_button(floor)

def floor_call():
    floor = select_floor()
    direction = select_direction()
    print("Floor call to",floor,"going",direction)
    b.floor_call(floor,direction)
    
def select_car():
    # menu for car selection
    car_options = []
    for f in range(1, b.number_cars + 1):
        # use shortcut keys for car numbers
        car_options.append("["+str(f)+"] "+str(f))

    car_menu = TerminalMenu(car_options,title="Elevator:")
    car_index = int(car_menu.show())
    car_index += 1
    car = int(car_index)
    return car

def select_floor():
    # menu for floor selection
    floor_options = []
    floors = []
    for f in range(b.levels,0,-1):
        # single digit floors get shortcut key
        if (f <= 9):
            floor_options.append("["+str(f)+"] "+str(f))
        # double digit floors, no shortcut key
        else:
            floor_options.append(str(f))
        floors.append(f)
    floor_menu = TerminalMenu(floor_options,title="floor:")
    floor_index = floor_menu.show()
    floor = floors[floor_index]
    return floor

def select_direction():
    # menu for up/down selection
    direction_options = ["[u] up","[d] down"]
    direction_keys = ["up","down"]
    direction_menu = TerminalMenu(direction_options,title="direction:")
    direction_choice_index = direction_menu.show()
    direction = direction_keys[direction_choice_index] 
    return direction

def do_quit():
    print (f"Thanks for using {TITLE}")
    quit()

def main():
    main_options = ["[r] run timestep","[b] press elevator button","[d] toggle doors","[t] teleport","[q] quit","[c] floor call"]
    main_functions = ['b.run()','press_button()','toggle_doors()','teleport()','do_quit()','floor_call()']
    main_menu = TerminalMenu(main_options)
    run = True
    while (run):
        show_title()
        b.display()
        choice_index = main_menu.show()
        # execute function corresponding to menu choice.  Indexes of main_options and main_functions are synched
        eval(main_functions[choice_index])

def setup():
    show_title()
    print("Setup:")
    el = input("number of elevators:")
    fl = input("number of floors:")
    # defaults if user just presses enter to questions
    if (el == ""):
        el = 4
    if (fl == ""):
        fl = 8
    el = int(el)
    fl = int(fl)
    b = bank(fl,el)
    return b

b = setup()
main()
