class stationery:
    def __init__(self, name, function, ink, price, quantity):
        self.name = name
        self.function = function
        self.ink = ink
        self.price = price
        self.quantity = quantity
    def display_properties(self):
        print(self.name, self.function, self.ink, self.price, self.quantity)
    def total_cost(self):
        total_cost = self.price * self.quantity
        print(total_cost)
    def price_amount(self):
        self.price
        return self.price
        
pencil = stationery("pencil", "writing", False, 0.50, 5)
pencil.display_properties()
pencil.total_cost()
print(pencil.function)
price = pencil.price_amount()
print(price)

ruler = stationery("ruler", "measurement", False, 0.35, 4)
ruler.display_properties()
ruler.total_cost()
print(ruler.function)
price = ruler.price_amount()
print(price)
