class Customer:

    def __init__(self, age, gender):
        self.cust_age = age
        self.cust_gender = gender
        print("Customer is created with ", self.cust_age, self.cust_gender)

    def discount(self):
        print("Discount is {} %".format(0))


class PreferredCustomer(Customer):

    def __init__(self, age, gender, email, postal):
        Customer.__init__(self, age, gender)
        self.cust_email = email
        self.cust_postal = postal
        print("Email is {} and Postal address is {} ".format(self.cust_email, self.cust_postal))

    def discount(self):
        print("Discount for {} is {} %".format(self.cust_email, 5))

    def validate_address(self):
        print("USPS Based Address Validation for ", self.cust_postal)
        if len(self.cust_postal) > 10:
            return True
        else:
            return False

    def bank_validation(self):
        print("Customer carries another bank credit card ", self.cust_email)


class CreditScore:

    def __init__(self, ssn, name):
        self.cs_ssn = ssn
        self.cs_name = name
        print("CreditScore initialized for {} with {}".format(self.cs_name, self.cs_ssn))

    def check_credit(self):
        print("CreditScore:: Credit Check for SSN ", self.cs_ssn)
        return 823

    def bank_validation(self):
        print("How old is this account and other details will be fetched ", self.cs_ssn)


class CreditCardCustomer(PreferredCustomer, CreditScore):

    def __init__(self, age, gender, email, postal, name, ssn):
        PreferredCustomer.__init__(self, age, gender, email, postal)
        CreditScore.__init__(self,ssn, name)
        self.cust_name = name
        self.cust_ssn = ssn
        print("CreditCardCustomer is created with given SSN")

    def discount(self):
        print("Discount for {} is {} %".format(self.cust_name, 7))

    def validate_address(self):
        if PreferredCustomer.validate_address(self):
            print("Google Map Based Address Validation for ", self.cust_name)
        else:
            print("Google Map validation is not allowed for invalid addresses")

    def bank_validation(self):
        PreferredCustomer.bank_validation(self)
        CreditScore.bank_validation(self)
        print("CreditCardCustomer Bank Validation ", self.cs_ssn)


ccCust = CreditCardCustomer(35, 'M', 'abc@nbc.com', '33 Atlanta', 'Neil', '234902394')
ccCust.discount()
ccCust.validate_address()
ccCust.check_credit()
ccCust.bank_validation() # this method will be executed from first Parent - PreferredCustomer

print("CreditCardCustomer " , isinstance(ccCust, CreditCardCustomer))
print("PreferredCustomer " , isinstance(ccCust, PreferredCustomer))
print("CreditScore " , isinstance(ccCust, CreditScore))
print("Customer " , isinstance(ccCust, Customer))
print("object " , isinstance(ccCust, object))

print(" issubclass PreferredCustomer", issubclass(CreditCardCustomer, PreferredCustomer))
print(" CreditScore PreferredCustomer", issubclass(CreditCardCustomer, CreditScore))
print(" Customer PreferredCustomer", issubclass(CreditCardCustomer, Customer))
print(" object PreferredCustomer", issubclass(CreditCardCustomer, object))