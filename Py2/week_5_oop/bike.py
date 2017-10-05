class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def display_info(self):
        info = {
            'Price': self.price,
            'Max Speed': self.max_speed,
            'Total Miles': self.miles
        }

        print info


    def ride(self):
        print 'Riding'
        self.miles = self.miles + 10

        return self


    def reverse(self):
        print 'Reversing'
        self.miles = self.miles - 5

        return self



bike1 = Bike(100, 30, 100)
bike2 = Bike(50, 25, 75)
bike3 = Bike(75, 40, 60)

bike1.ride().ride().ride().reverse().display_info()
bike2.ride().ride().reverse().reverse().display_info()
bike3.reverse().reverse().reverse().display_info()
