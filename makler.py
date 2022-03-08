# coding=utf-8
class Apartment:
    def __init__(self):
        self.space = 0
        self.rooms = input("Anzahl Raeume: [Zahl]")


class Room:
    def __init__(self):
        self.rectangles = input("Anzahl Rechtecke? [Zahl]")
        #self.slopedRoof = input("Schraegdach?(nur unter einer Hoehe von 2 Metern) [1 für ja / 0 für nein]")


class Rectangle:
    def __init__(self):
        self.length = input("Laenge in Meter:")
        self.width = input("Breite in Meter:")
        self.space = self.width * self.length


class SlopedRectangle:
    def __init__(self):
        self.length = input("Länge in Meter:")
        self.width = input("Breite in Meter:")
        self.space = self.width * self.length * 0.5


class CalculationService:
    def calculateNonSlopedRoofRoom(self, room):
        if room.rectangles == 1:
            rectangle = Rectangle()
            apartment.space += rectangle.space
        else:
            for j in range(0, room.rectangles):
                rectangle = Rectangle()
                apartment.space += rectangle.space

    def calculateSlopedRoofRoom(self):
        if input("Gibt es eine Fläche an der die Decke zwischen 1 und 2 Meter hoch ist? [1 für ja / 0 für nein]") == 1:
            amount = input("Anzahl Rechtecke in die sich dieser Bereich unterteilen lässt?")
            for y in range(0, amount):
                slopedRectangle = SlopedRectangle()
                apartment.space += slopedRectangle.space
        if input("Gibt es noch eine Fläche an der die Decke über 2 Meter hoch ist? [1 für ja / 0 für nein]") == 1:
            room = Room()
            room.slopedRoof = 0
            self.calculateNonSlopedRoofRoom(Room())


apartment = Apartment()
calculationService = CalculationService()

for i in range(0, apartment.rooms):
    print "Raum " + str(i + 1)
    room = Room()
    #if room.slopedRoof == 0:
    calculationService.calculateNonSlopedRoofRoom(room)
    #else:
     #   calculationService.calculateSlopedRoofRoom()

print apartment.space
