import product


class Phone(product.Product):
    def __init__(self, name, price, ram, cpu):
        product.Product.__init__(self, name, price)
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.price=price

    def __str__(self):
        """
        TODO:
            * supraincarca metoda str

        Returns:
            * str:    un string ce va contine informatiile
                      specifice telefonului (nume, CPU, RAM)
        """
        return f"The new {self.name} is an unforgettable experience, CPU {self.cpu}, RAM {self.ram}."
