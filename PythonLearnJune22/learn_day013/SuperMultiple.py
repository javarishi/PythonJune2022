class Base1:

    def __init__(self, name):
        self.name = name
        print("Base 1", self.name)


class Base2:
    def __init__(self, name):
        self.name = name
        print("Base 2", self.name)
        
    
class SubClass(Base1, Base2):
    
    def __init__(self, name):
        super(SubClass, self).__init__(name)
        print("Subclass ",  self.name)


instance = SubClass("Something")