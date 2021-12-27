# Sublcass of elevator for the elevator bank, which controls one or more elevator cars.  
# cars are a separate subclass

from elevators import elevator
from cars import car

class bank(elevator):
    def __init__(self, levels, cars):
        self.number_cars = cars
        self.levels = levels
        # initialize cars dictionary indexed by number.  Starts at 1, goes to number of cars
        self.cars = {i: car(self.levels) for i in range(1,self.number_cars + 1)}

    def display(self):
        frame_buffer = ""
        frame_buffer += self.header()
        frame_buffer += self.body()
        print(frame_buffer)

    def header(self):
        status = " " * self.STATUSWIDTH
        main_header = ""
        halfcar = int((self.CARWIDTH - 1) / 2) 
        padding = f"{(halfcar) * ' '}"
        # car numbers centered on shafts
        for i in range(1, self.number_cars + 1):
            main_header += f" {padding}{str(i)}{padding}"
        line_buffer = f"{status}{main_header}\n"
        return line_buffer

    def body(self):
        line_buffer = ""
        for floor in range(self.levels, 0, -1):
            line_buffer += self.show_floor(floor)
        return line_buffer

    def show_floor(self,floor):
        # status area
        pad = (self.STATUSWIDTH - len(str(floor))) * " "
        status = f"{str(floor)}{pad}"
        # elevator shafts with empty areas or cars
        main_floor = ""
        for car in range(1,self.number_cars + 1):
            if self.cars[car].location == floor:
                shaftcontents = self.cars[car].display() 
            else:
                shaftcontents = self.CARWIDTH * " "
            # left wall and shaft display
            main_floor += f"|{shaftcontents}"
        line_buffer = f"{status}{main_floor}|\n"
        return line_buffer

    def run(self):
        # do bank run tasks
        for car in range(1, self.number_cars + 1):
            self.cars[car].run()

    def floor_call(self,floor,direction):
        car = 1
        self.cars[car].floor_call(floor,direction)

if __name__ == "__main__":
    b = bank(8, 5)
    print(b.number_cars,"Cars on", b.levels,"Floors.")
    b.cars[5].doors_open = False
    b.cars[5].location = 1
    b.cars[4].location = 7
    b.cars[4].doors_open = False
    b.cars[3].doors_open = False
    b.cars[3].location = 3
    b.cars[2].location = 8
    b.display()
