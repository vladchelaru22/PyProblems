class Cart:
    def __init__(self):
        self.list_cart = []

    def add(self, new_product):
        if new_product not in self.list_cart:
            self.list_cart.append(new_product)
        """
        TODO 1:
            * adauga un produs in lista de cumparaturi list_cart

        Args:
            * new_product (Product):    produsul ce va fi adadugat in cart

        """

    def remove(self, product_name):
        for product in self.list_cart:
            if product.name == product_name:
                self.list_cart.remove(product)
        """
        TODO 2:
            * sterge produsul din lista de cumparaturi list_card

        Args:
            * product_name (str):    numele produsului ce va fi scos din cart

        """

    def view(self):
        return self.list_cart

    def cart_checkout(self):
        """
        TODO 3:
            * calculeaza suma preturilor tuturor produselor din cart
            * goleste cartul (in urma cart_checkout, cartul va fi gol)

        Return:
            * int:    suma preturilor tuturor produselor din cart
        """
        suma = 0
        for product in self.list_cart:
            suma += product.price
        self.list_cart.clear()
        return suma
