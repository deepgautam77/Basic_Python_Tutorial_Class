#Write a function called describe_city() that accepts the name of a city and its country
#eg: Kathmandu is in Nepal
#give country a default value
#Call the function and write city of another country. (Change default value)

def place(city, country='Nepal'):
    details= ("You live in "+city+","+ country)
    return str(details)

place('Itahari')     #called place function with its default value in it.
place('Dharan')
place('Biratchowk')

za=place(city='Delhi', country='India') #changed the default value of country
print(za)