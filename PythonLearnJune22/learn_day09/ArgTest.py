def validate_address(*args):
    print(args, type(args))
    # args - unlimited number of argument tuple
    for eachValue in args:
        print(eachValue)

# Any number of parameters can accept
validate_address("3375", "Paces Ferry Road", "Cumlerland Pwky", "Atlanta", "GA", "30080")