class Calculator:
    def __init__ (self, batteryMax:int):
        self.battery: int = 0
        self.display: float = 0
        self.batteryMax: int = batteryMax

    def __str__ (self):
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def charge(self,chargeBattery: int):
        self.battery += chargeBattery
        if self.battery >= self.batteryMax:
            self.battery = self.batteryMax
       
    def sum (self, a: float, b:float):
         if self.battery <= 0:
             print ("fail: bateria insuficiente")
         else:
             self.display = (a) + (b)
             self.battery -= 1
         
             

    def div (self, num:float, div:float):
        if self.battery <= 0:
            print ("fail: bateria insuficiente")
            return
        elif div == 0:
            print ("fail: divisao por zero")
            self.battery -= 1
            return
        self.display = num / div
        self.battery -= 1
    


def main ():
    calculadora = Calculator(0)
    while True:
        line: str = input()
        print ("$"+ line)
        args: list[str] = line.split(" ")
        if args [0] == "end":
            break
        elif args [0] == "init":
            batteryMax: int = int(args[1])
            calculadora =  Calculator(batteryMax)
        elif args [0] == "show":
            print(calculadora)
        elif args [0] == "charge":
            chargeBattery: int = int(args[1])
            calculadora.charge(chargeBattery)
        elif args [0] == "sum":
           a: float = float(args[1])
           b: float = float(args[2])
           calculadora.sum(a,b)
        elif args [0] == "div":
            num: float = float(args[1])
            div: float = float(args[2])
            calculadora.div(num,div)

main()