class car:

    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f"New {self.color} {self.name} is born!")

    def go(self):
        print(f"{self.color} car {self.name} is going")

    def show_speed(self):
        print(f"{self.color} car {self.name} speed is {self.speed}")

    def stop(self):
        self.speed = 0
        print(f"{self.name} is stopped")

    def turn(self,direction):
        self.direction = direction
        print(f"{self.color} car {self.name} turn {self.direction}")

class TownCar(car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} -Over speed!")

class WorkCar(car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} - Over speed!")

class SportCar(car):
    pass

class PoliceCar(car):
    pass

TCar = TownCar(70, 'red', 'ford focus', False)
WCar = WorkCar(50, 'blue', 'nissan', False)
PCar = PoliceCar(150,'black','Ford Mustang',True)
TCar.go()
TCar.turn("left")
TCar.show_speed()
TCar.stop()
WCar.show_speed()
PCar.show_speed()
