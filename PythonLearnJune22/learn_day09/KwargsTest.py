def validate_address(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key, value)


validate_address(houseNum="3375",
                addLine1="Paces Ferry Road",
                addLine2="Cumlerland Pwky",
                 city="Atlanta",
                 state= "GA",
                 zipcode="30080")