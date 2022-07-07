class Customer:

    def __init__(self, custName="Neil", custAge=21, custStore="Pharmacy"):
        self.custId = '000'
        self.name = custName
        self.age = custAge
        self.store = custStore
        print(self.name, self.age, self.store, self.custId)

    def discount(self):
        print("{} ,Your discount is  {} % ".format(self.name, 0))

    def purchase(self, total):
        print("Customer {}, total is {}$".format(self.name, total))


# Self is param / arg represents object on which this method is being called
# creating object / instance
# objectName = ClassName() object used . operator to access variables and functions
cust01 = Customer()
cust01.discount()
# Customer() --> implicit special function is being called - Constructor
cust02 = Customer()
cust02.name = "David"
cust02.age = 40
cust02.store = "CVS"
cust02.discount()

cust03 = Customer("Buzz", 40, "Walgreens")
cust03.discount()
cust03.purchase(100)
