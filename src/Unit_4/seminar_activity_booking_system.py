#
# Activity for seminar for a holiday booking system.
#

class Employee:
    """Parent class for retaining employee details and allowing booking of annual leave/holidays."""
    def __init__(self, employee_id: str, grade: str, holiday_allowance: int):
        """Initialising employee object."""
        self.employee_id = employee_id
        self.grade = grade
        self.holiday_allowance = holiday_allowance
        self.booked_holidays = 0

    def book_holidays(self, days):
        """Reduce holiday allowance, but actual booked days pending."""
        self.holiday_allowance -= days
        print(f"Booked {days} days of leave. Holiday allowance reduced to {self.holiday_allowance} days.")


class Manager(Employee):
    """Child class for defining specific Manager attributes and methods."""
    def __init__(self, employee_id: str, grade: str, holiday_allowance: int, num_reportees):
        super().__init__(employee_id, grade, holiday_allowance)
        self.num_reportees = num_reportees

    @staticmethod
    def approve_holidays(employee, days):
        """Method for approving holidays. Adds the days to employee's booked holidays."""
        employee.booked_holidays += days
        print(f"Holidays approved. Employee booked holidays increased to {employee.booked_holidays} days.")

    @staticmethod
    def reject_holidays(employee, days):
        """Method for rejecting holidays. Method returns holidays back into employee's allowance."""
        employee.holiday_allowance += days
        print(f"Holidays rejected. Employee holiday allowance increased back to {employee.holiday_allowance} days.")


class Company:
    """Class to hold company attributes and any relevant methods."""
    def __init__(self, name, num_employess):
        """Initialise company class"""
        self.name = name
        self.num_employees = num_employess


if __name__ == '__main__':
    # initialise Company instance
    comp = Company("ACME Co.", 20)
    # initialise employee and manager instances
    employee1 = Employee("123", "C1", 25)
    manager1 = Manager("456", "A1", 25, 5)

    # activities
    employee1.book_holidays(5)
    manager1.approve_holidays(employee1, 5)
