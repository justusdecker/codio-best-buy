from products import Product
class Store:
    """
    A Class that will manage Products
    """
    def __init__(self):
        self.products = [
            Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            Product("MacBook Air M2", price=1450, quantity=100),
            Product("A Big Tasty Bacon🍔", price=250, quantity=500)] #I'm hungry 🤤
    def remove_product(self):
        pass
    def get_total_quantity(self) -> int:
        return sum([i.get_quantity() for i in self.products])
    def get_all_products(self) -> int:
        return sum([i.is_active() for i in self.products])
    def order(self):
        pass