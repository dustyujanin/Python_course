class Stationery:
    def __init__(self,title="title"):
        self.title = title
    def draw(self):
        print("Start painting")

class Pen(Stationery):
    def draw(self):
        self.title = "Pen"
        print(f"{self.title} painting")

class Pencil(Stationery):
    def draw(self):
        self.title = "Pencil"
        print(f"{self.title} painting")

class Handle(Stationery):
    def draw(self):
        self.title = "Handle"
        print(f"{self.title} painting")

Pen = Pen()
Pen.draw()

Pencil = Pencil()
Pencil.draw()

Handle = Handle()
Handle.draw()