# You cannot have *args after **kwargs
def validate_address(city, zipcode,*args, **kwargs):
    print(city, zipcode)
    print("** Args Starts here **")
    if len(args) > 0 :
        for eachValue in args:
            print(eachValue)
    print("** Kwargs Starts here **")
    if len(kwargs) > 0:
        for key, value in kwargs.items():
            print(key, value)


# Positional Argument cannot be declared after kw argument
# kw arguments are always declared at the end
validate_address("Atlanta",33080,houseNum="3375",addLine1="Paces Ferry Road", addLine2="Cumlerland Pwky",state= "GA")