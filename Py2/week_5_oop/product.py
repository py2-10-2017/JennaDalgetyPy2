class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self):
        sales_tax = .10
        tax_amount  = sales_tax * self.price
        self.price += tax_amount
        return self

    def display_info(self):
        print "Brand:", self.brand
        print "Name:", self.item_name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Cost:", self.cost
        print "Status:", self.status

    def item_return(self, reason):

        if reason == "defective":
            self.status = "defective"
            self.price = 0
        if reason == "boxed":
            self.status = "for sale"
        if reason == "opened":
            self.status = "used"
            discounted_price = self.price * .20
            self.price -= discounted_price
        return self



product1 = Product(15, "Cat Litter", "20lbs", "Tidy Cat", 7)

product1.add_tax().display_info()
