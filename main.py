import random

class Unit_Create():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{}이 1기 생성되었습니다".format(self.name))
        print("[체력 : {} / 공격력 : {}]".format(self.hp, self.damage))

    def getDamaged(self):
        damage = random.randint(1, 55)
        self.hp = self.hp - damage
        print("{}의 데미지를 받았습니다".format(damage))
        print("남은 체력은 {}입니다".format(self.hp))


m1 = Unit_Create("해병", 40, 5)

m1.getDamaged()
m1.getDamaged()