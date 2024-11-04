from math import pi

def area_of_circle(radius):
    result = pi * radius ** 2
    return round(result, 2)

def display_radius():
    while True:
        try:
            user_input = int(input("\nPlease type your circle's radius below.\n"))
            print(f"\nThe area of this circle is {area_of_circle(user_input)}\n")
            break
        except:
            user_input = TypeError
            print("\nPlease type a numerical value.")

def loop_program():
    while True:
        cont = input("Would you like to calculate the area of another circle? (Y/N):\n").strip().lower()
        if cont == "y":
            display_radius()
        elif cont == "n":
            print("\nThanks for using this program! Goodbye.")
            break
        else:
            print('\nPlease type either "Y" or "N"\n')

def main():
    display_radius()
    loop_program()

main()
