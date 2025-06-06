class Product:
    """
    A product will have:
    ---
    - A name    **cannot be empty**   ``str``
    - A price   **cannot below 0**    ``float | int``
    - A quanity **cannot below 0**    ``int``
    """
    def __init__(self,
                 name : str,
                 price : float,
                 quantity : int) -> None:
        
        self.set_name(name)
        self.set_price(price)
        self.set_quantity(quantity)
        self.active : bool = False
    def _check_name(self,value: str) -> None:
        """
        Will check for edge cases before ``name`` will be set
        ---
        
        will raise a ``TypeError`` if value is not ``str``
        
        will raise a ``ValueError`` if value is empty
        """
        # Typecheck: name
        if not isinstance(value, str):
            raise TypeError(f"{value} is not a string!")
        # Valuecheck: name
        if not value:
            ValueError("Name cannot be empty!")
    def _check_price(self,value: float | int) -> None:
        """
        Will check for edge cases before ``price`` will be set
        ---
        
        will raise a ``TypeError`` if value is not ``int`` or ``float``
        
        will raise a ``ValueError`` if value is below 0
        """
        # Typecheck: price
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError(f"{value} is not numeric!")
        # Valuecheck: price
        if value < 0:
            raise ValueError(f"Price can't be below Zero!")
    def _check_quantity(self,value: int) -> None:
        """
        Will check for edge cases before ``quantity`` will be set
        ---
        
        will raise a ``TypeError`` if value is not ``int``
        
        will raise a ``ValueError`` if value is below 0
        """
        # Typecheck: quantity
        if not isinstance(value, int):
            raise TypeError(f"{value} is not an integer!")
        # Valuecheck: quantity
        if value < 0:
            raise ValueError(f"Price can't be below Zero!")

    def get_quantity(self) -> int | float:
        return self.quantity
    
    def set_quantity(self,value: int) -> None:
        self._check_quantity()
        self.quantity = value

    def get_price(self) -> int | float:
        """ Get the price of the product """
        return self.price
    
    def set_price(self,value: int | float) -> None:
        """ Set the price of the product """
        self._check_price()
        self.price = value
    
    def get_name(self) -> str:
        """ Get the name of the product """
        return self.name
    
    def set_name(self,value: str) -> None:
        """ Set the name of the product """
        self._check_name()
        self.name = value

    def activate(self) -> None:
        self.active = True
    
    def deactivate(self) -> None:
        self.active = False

    def is_active(self) -> bool:
        return self.active

    def show(self) -> str:
        return f"{self.name:<15}{self.price:<6}{self.quantity:<15}" # titles like name, price & quanity will be printed in the main function! Looks better!
    
    def buy(self,quantity: int) -> float | int:
        if not isinstance(quantity,int):
            raise TypeError("Quantity is not an integer!")
        if quantity < 0:
            raise ValueError("Quantity cannot below 0")
        if quantity > self.quantity: # caps at maximum quantity. No exception needed!
            quantity = self.quantity
        self.quantity -= quantity
        return quantity * self.price