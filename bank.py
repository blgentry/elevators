# Sublcass of elevator for the elevator bank, which controls one or more elevator cars.  
# cars are a separate subclass

from elevators import elevator
from cars import car

class bank(elevator):
    def __init__(self, levels, cars):
        self.number_cars = cars
        self.levels = levels
        self.cars = []
        self.cars.append("dummy")
        for i in range(1, self.number_cars + 1):
            self.cars.append(car(self.levels))

    def display(self):
        frame_buffer = ""
        frame_buffer += self.header()
        frame_buffer += self.body()
        print(frame_buffer)

    def header(self):
        line_buffer = ""
        line_buffer += " " * self.STATUSWIDTH
        halfcar = int((self.CARWIDTH - 1) / 2) 
        for i in range(1, self.number_cars + 1):
            # account for wall
            line_buffer += " "
            line_buffer += " " * halfcar
            line_buffer += str(i)
            line_buffer += " " * halfcar
        line_buffer += "\n"
        return line_buffer

    def body(self):
        line_buffer = ""
        for floor in range(self.levels, 0, -1):
            line_buffer += self.show_floor(floor)
        return line_buffer

    def show_floor(self,floor):
        line_buffer = ""
        # floor number 
        line_buffer += str(floor)
        # pad status area
        pad = (self.STATUSWIDTH - len(str(floor))) * " "
        line_buffer += pad
        for car in range(1,self.number_cars + 1):
            # left wall
            line_buffer += "|"
            # car
            if self.cars[car].location == floor:
                line_buffer += self.cars[car].display() 
            else:
                line_buffer += self.CARWIDTH * " "

        # last wall
        line_buffer += "|"
        line_buffer += "\n"
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
    b.cars[5].doors_open = 0
    b.cars[5].location = 1
    b.cars[4].location = 7
    b.cars[4].doors_open = 0
    b.cars[3].doors_open = 0
    b.cars[3].location = 3
    b.cars[2].location = 8
    b.display()
