from animal import Animal


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print str(self.health) + " I am a dragon"


dog1 = Dog("Air Bud")
dog1.walk().walk().walk().run().run().display_health()

dragon1 = Dragon("Smaug")
dragon1.fly().display_health()