class Stock:
    def __init__(self, list_stock):
        self.list_stock = []
        for product in list_stock:
            self.list_stock.append(product)

    def add(self, new_product):
        if new_product not in self.list_stock:
            self.list_stock.append(new_product)
        """
        TODO 1:
            * adauga un produs nou in stoc

        Args:
            * new_product (Product):    noul produs de adaugat in stoc

        """

    def remove(self, product_name):
        for product in self.list_stock:
            if product.name == product_name:
                self.list_stock.remove(product)
        """
        TODO 2:
            * sterge din stocul magazinului produsul dat ca parametru

        Args:
            * product_name (str):    numele produsului urmeaza a fi sters

        """

    def view(self):
        """
        TODO 3:
            * returneaza stocul curent

        Returns:
            * [Product]:    lista de produse din stoc

        """
        return self.list_stock