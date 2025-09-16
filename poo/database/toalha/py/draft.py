class Towel:
    def __init__ (self):
        self.color="red"
        self.size="p"
        self.wetness= 0

    def __str__(self):
        return f"color:{self:color}, tam:{self.size}, hum:{self.wetness} "
    
towel = Towel()
print(towel.color)
print(towel.size)
print(towel.wetness)

print (Towel)