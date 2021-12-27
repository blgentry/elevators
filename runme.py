from bank import bank
from simple_term_menu import TerminalMenu

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
		car_options.append(str(f))

	car_menu = TerminalMenu(car_options,title="Elevator:")
	car_index = int(car_menu.show())
	car = int(car_options[car_index])
	return car

def select_floor():
	# menu for floor selection
	floor_options = []
	for f in range(b.levels,0,-1):
		floor_options.append(str(f))

	floor_menu = TerminalMenu(floor_options,title="Floor:")
	floor_index = floor_menu.show()
	floor = int(floor_options[floor_index])
	return floor

def select_direction():
	# menu for up/down selection
	direction_options = ["[u] up","[d] down"]
	direction_keys = ["up","down"]
	direction_menu = TerminalMenu(direction_options,title="Direction:")
	direction_choice_index = direction_menu.show()
	direction = direction_keys[direction_choice_index] 
	return direction


def main():
	main_options = ["[r] run timestep","[t] teleport","[c] floor call","[b] press elevator button","[d] Toggle Doors","[q] quit"]
	main_menu = TerminalMenu(main_options)
	RUN = True
	while (RUN):
		b.display()
		choice_index = main_menu.show()
		choice = main_options[choice_index]
		if choice == "[q] quit":
			RUN = False
		elif choice == "[r] run timestep":
			b.run()
		elif choice == "[t] teleport":
			teleport()
		elif choice == "[c] floor call":
			floor_call()
		elif choice == "[d] Toggle Doors":
			toggle_doors()
		elif choice == "[b] press elevator button":
			press_button()

def setup():
	print("Elevator Bank Setup\n")
	el = input("Number of Elevators:")
	fl = input("Number of Floors:")
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
