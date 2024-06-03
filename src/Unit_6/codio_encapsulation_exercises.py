#
# Codio exercises on encapsulation
#

class Country:
    """Country class with private name, capital, population and continent attributes."""
    def __init__(self, name, capital, population, continent):
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent


class BankAccount:
    """Bank account class with private checking and savings attributes."""
    def __init__(self, checking=0, savings=0):
        self._checking = checking
        self._savings = savings

    # getter methods
    def get_checking(self):
        return self._checking

    def get_savings(self):
        return self._savings

    # setter methods
    def set_checking(self, amount):
        self._checking = amount

    def set_savings(self, amount):
        self._savings = amount


class Cyclist:
    """Cyclist class with hidden name, nationality and nickname attributes."""
    def __init__(self, name, nationality, nickname):
        self._name = name
        self._nationality = nationality
        self._nickname = nickname

    # getter and setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    # getter and setter for nationality
    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, new_nat):
        self._nationality = new_nat

    # getter and setter for nickname
    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, new_nick):
        self._nickname = new_nick


if __name__ == '__main__':
    my_country = Country('France', 'Paris', 67081000, 'Europe')
    print(my_country._name)
    print(my_country._capital)
    print(my_country._population)
    print(my_country._continent)

    my_account = BankAccount()
    my_account.set_checking(523.48)
    print(my_account.get_checking())
    my_account.set_savings(386.15)
    print(my_account.get_savings())

    my_cyclist = Cyclist("Greg LeMond", "American", "Le Montstre")
    print(my_cyclist.name)
    my_cyclist.name = "Eddy Merckx"
    print(my_cyclist.name)