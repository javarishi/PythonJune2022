class Address:
    def __init__(self, address):
        self.address = address
        print("Address provided ", address)


class ValidAddress(Address):
    def __init__(self, address):
        super().__init__(address)
        print("Zipcode is provided with ", self.address)


class ValidNumber(Address):
    def __init__(self, address):
        super().__init__(address)
        print("house_number is provided with ", self.address)


class CustomerAddress(ValidAddress, ValidNumber):
    def __init__(self, address):
        super().__init__(address) # Super will execute all matching parents 
        print("DONE!")


cust01 = CustomerAddress("1234 Somebody Blvd, FewCity 99887")
