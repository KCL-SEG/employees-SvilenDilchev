"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthlySalary = 0, hourlySalary = 0, hoursWorked = 0, bonusCommission = 0, payPerContract = 0, contractCount = 0):
        self.name = name
        self.monthlySalary = monthlySalary
        self.hourlySalary = hourlySalary
        self.hoursWorked = hoursWorked
        self.bonusCommission = bonusCommission
        self.payPerContract = payPerContract
        self.contactCount = contractCount

    def get_pay(self):
        return self.monthlySalary + self.hourlySalary * self.hoursWorked + self.bonusCommission + self.payPerContract * self.contactCount

    def __str__(self):

        output = f"{self.name} works on a "
        if self.monthlySalary > 0:
            output += f"monthly salary of {self.monthlySalary}"

        if self.hourlySalary > 0:
            output += f"contract of {self.hoursWorked} hours at {self.hourlySalary}/hour"

        if self.bonusCommission > 0:
            output += f" and receives a bonus commission of {self.bonusCommission}"

        if self.payPerContract > 0:
            output += f" and receives a commission for {self.contactCount} contract(s) at {self.payPerContract}/contract"

        output += f". Their total pay is {self.get_pay()}."
        return output


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthlySalary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hourlySalary=25, hoursWorked=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', monthlySalary=3000, payPerContract=200, contractCount=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hourlySalary=25, hoursWorked=150, payPerContract=220, contractCount=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', monthlySalary=2000, bonusCommission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hourlySalary=30, hoursWorked=120, bonusCommission=600)
