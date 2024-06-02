#
# Develop a Python program and apply protected and unprotected variables within it.
#

class FoodCupboard:
    """The class for storing cupboard objects."""
    cupboard_location = "Kitchen"
    capacity = 20

    def __init__(self, items: list):
        """Cupboard initialised as a list with items."""
        self._items = items

    # Public method to display cupboard details
    def display_cupboard_details(self):
        """Method for displaying cupboard details."""
        print(f"Cupboard Name: {self.cupboard_location}")
        print(f"Cupboard can store up to {self.capacity} items")
        print(f"Items: {', '.join(self._items)}")


if __name__ == '__main__':
    new_cupboard = FoodCupboard(["Spaghetti", "Canned tomatoes", "Dried basil"])
    new_cupboard.display_cupboard_details()

