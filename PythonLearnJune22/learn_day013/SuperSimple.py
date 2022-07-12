# Parent class = Base Class = Super class
# Child Class = Subclass 

class Simple:

    def __init__(self):
        print("Simple class Constructor")

    def dummy_method(self):
        print("Super class dummy method")


class SuperSimple(Simple):
    def __init__(self):
        super().__init__()
        print("Super Simple Constructor")


ssp = SuperSimple()