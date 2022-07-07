def validate_address(city, zipcode, street):
    print("Street : {} , City : {} , zipcode : {} ".format(street, city, zipcode))

# named parameters - keyword parameters - keyword arguments
validate_address(zipcode=33080, city="Atlanta", street="Paces Ferry Road")