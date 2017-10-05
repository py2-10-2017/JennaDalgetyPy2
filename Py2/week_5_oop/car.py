class Car(object):
  def __init__(self, price, speed, fuel, mileage):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
    self.tax = self.check_tax()

  def check_tax(self):
    if self.price > 10000:
      tax = .15
    else:
      tax = .12

    return tax * self.price

  def display_all(self):
    info = {
      'Price': self.price,
      'Speed': self.speed,
      'Fuel': "Full",
      'Mileage': '15 MPG',
      'Tax': self.tax
    }
    return info

toyota = Car(12000, '35 MPH', 'Full', '25 MPG')
honda = Car(9000, '40 MPH', 'Empty', '30 MPG')
bmw = Car(30000, '40 MPH', 'Half-Full', '20 MPG')
acura = Car(19000, '60 MPH', 'Full', '35 MPG')
dodge = Car(5000, '30 MPH', 'Empty', '20 MPG')
audi = Car(45000, '40 MPH', 'Full', '30 MPG')

cars = [toyota, honda, bmw, acura, dodge, audi]

for car in cars:
  info = car.display_all()
  for attribute in info:
    print attribute + ': ' + str(info[attribute]) + '.'

  print '-' * 20