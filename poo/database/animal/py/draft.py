class Animal:
    def __init__(self, species: str, noise: str):
        self.species: str = species
        self.noise: str = noise
        self.age: int = 0

    def __str__ (self) -> str:
        return f"{self.species}:{self.age}:{self.noise}"  

    def ageBy (self, increment: int):
        self.age += increment
        if self.age >= 4:
            print (f"warning: {self.species} morreu")
            self.age = 4

    def makeSound(self):
        if self.age == 0:
            return ("---")
        if self.age >= 4:
            return ("RIP")
        else:
            return self.noise        

def main():
    bicho = Animal("","")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split (" ")
        if args [0] == "end":
            break
        elif args [0] == "init":
            species = args[1]
            sound = args[2]
            bicho = Animal(species,sound)
        elif args [0] == "show":
            print(bicho)
        elif args [0] == "grow":
            increment: int = int(args[1])
            bicho.ageBy(increment)
        elif args[0] == "noise":
           print (bicho.makeSound())
main()