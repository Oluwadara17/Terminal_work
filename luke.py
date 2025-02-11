import sys

input = sys.argv[1]
relations = {'Darth Vader' : 'father', 'Leia': 'sister', 'Han':'brother in law','R2D2':'droid', 'Rey': 'Padawan', 'Tatooine': 'homeworld'}
def main():
    if input == "Darth Vader":
        print('No, I am your father')
    else:
        print(f"Luke, I am your {relations[input]}")


main()