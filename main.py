def my_name():
    print("my name is mariam ")

my_name()

def my_meal(food,drink):
    print(f"I like to eat {food} and while drinking {drink}")

my_meal("chcolota", "water")


def cube(number):
    return(number**3)

def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False

print(by_three(7))