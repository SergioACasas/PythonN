class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name) # this in Java
ri = Robot("Sergio","red",77)
r2 = Robot("Pepe","Blue",11)
ri.introduce_self()
r2.introduce_self()
print(ri.color)