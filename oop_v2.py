class Pizza:
    def __init__(self, ingrd):
        self.ingrd = ingrd

    @classmethod
    def veg(cls):
        return cls(["tomatos", "olives", ])

    @classmethod
    def mrgt(cls):
        return cls(["meat", "olives", ])

    def __str__(self):
        return f"Pizza ingredient are {self.ingrd} "


pizza_veg = Pizza(["cucamber", "chille"])
pizza_me = Pizza.veg()

print(pizza_veg, pizza_me)
