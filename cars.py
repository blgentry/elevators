from elevators import elevator

class car(elevator):
    def __init__(self,levels):
        self.levels = levels
        self.travel = 0
        self.location = 1
        self.doors_open = 1
        self.queue = []
        self.queueup = []
        self.queuedown = []
        self.state = "READY"

    def display(self):
        line_buffer = ""
        if self.doors_open == 1:
            # doors open
            line_buffer = f"]{(self.CARWIDTH - 2) * ' '}["
        else:
            # doors shut
            halfwidth = f"{int((self.CARWIDTH - 3)/2) * ' '}"
            line_buffer = "[{halfwidth}|{halfwidth}]"

        return(line_buffer)

    def run(self):
        if self.state == "READY":
            self.do_ready()
        elif self.state == "RUN":
            self.do_run()
        elif self.state == "RUN_LAND":
            self.do_run_land()

    def do_ready(self):
        #print("I'm READY")
        if self.queueup != []:
            self.queue = self.queueup
            self.travel = 1
            self.doors_open = 0
            self.state = "RUN"
        elif self.queuedown != []:
            self.queue = self.queuedown
            self.travel = -1
            self.doors_open = 0
            self.state = "RUN"

    def press_button(self, floor):
        if (floor - self.location) > 0 :
            # check for duplicate entry
            if floor not in self.queueup:
                    self.queueup.append(floor)
                    self.queueup.sort()
                    #print("Added",floor,"to queueup")
                    #print(self.queueup)
        elif (floor - self.location) < 0 :
            # check for duplicate entry
            if floor not in self.queuedown:
                    self.queuedown.append(floor)
                    self.queuedown.sort()
                    self.queuedown.reverse()
                    #print("Added",floor,"to queuedown")
                    #print("location:",self.location)
                    #print("queue:",self.queuedown)

    def floor_call(self,floor,direction):
        if direction == "up":
            pass
        elif direction == "down":
            pass

    def do_run(self):
        target = self.queue[0]
        if (target == self.location):
            self.queue.remove(target)
            self.state = "RUN_LAND"
            self.doors_open = 1
        else:
            self.location += self.travel

    def do_run_land(self):
        self.doors_open = 0
        if self.queue == []:
            #print("queue is empty")
            if self.queueup != []:
                #print("queueUP has entries")
                self.queue = self.queueup
                self.travel = 1
                self.state = "RUN"

            if self.queuedown != []:
                #print("queueDOWN has entries")
                self.queue = self.queuedown
                self.travel = -1
                self.state = "RUN"
            else: 
                self.state = "READY"
                self.doors_open = 1
        else:
            self.state = "RUN"
        

if __name__ == "__main__":
    c = car(8)
    print("I have",c.levels,"floors.")
    print("Doors open  :", c.display())
    c.doors_open = 0
    print("Doors closed:", c.display())


            

