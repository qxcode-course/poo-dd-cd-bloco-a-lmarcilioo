class Car:
    def __init__(self, Pass: int, gas: int, km: int):
        self.Pass: int = 0
        self.gas: int = 0
        self.km: int = 0

    def __str__ (self) -> str:
        return f"pass: {self.Pass}, gas: { self.gas}, km: {self.km}"
    
    def passMax(self, amount: int):
        self.Pass += amount
        if self.Pass > 2:
            print ("fail: limite de pessoas atingido")
            self.Pass -= 1

    def leave(self, less: int):
        self.Pass -= less
        if self.Pass < 0:
            print ("fail: nao ha ninguem no carro")
            self.Pass += 1
           

def main():
    carro = Car( 0, 0, 0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split (" ")
        if args [0] == "end":
            break
        elif args [0] == "show":
            print(carro)
        elif args [0] == "enter":
            amount: int =int(1)
            carro.passMax(amount) 
        elif args [0] == "leave":
            less: int= int(1)
            carro.leave(less)

main()