def my_func(name, family, year, city, email, phone):
    print(f"{name} {family} {year} {city} {email} {phone}")


name = input("Enter your name: ")
family = input("Enter your family: ")
year = input("Enter your year: ")
city = input("Enter your city: ")
email = input("Enter your email: ")
phone = input("Enter you phone: ")
my_func(phone=phone, city=city, year=year, email=email, name=name, family=family)
