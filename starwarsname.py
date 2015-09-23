# Evan Sauers
# starwarsname.py
# Week 3: Star Wars Name Assignment

# This program gives you your Star Wars name.

# Prompt the user to input their Last and First name and their mother's maiden name and the city where they where born.

def main():
    print("This program gives you your Star Wars Name.")
    lastName = input("Please enter your last name: ")        # Calculate their "Star Wars" name.
    firstName = input("Please enter your first name: ")
    mothersName = input("Please enter your mother's maiden name: ")
    cityName = input("Please enter your city in which you were born: ")
    
    print(lastName[0:3] + firstName[0:2], mothersName[0:2] + cityName[0:3])        # Print out their "Star Wars" name.

main()






