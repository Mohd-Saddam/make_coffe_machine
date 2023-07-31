VALID_COFFEE_NAMES = ['latte', 'cappuccino', 'espresso']

def is_valid_note(note):
    valid_notes = {5, 10, 20, 50}
    return note in valid_notes

def is_valid_coffee_name(name):
    return name in VALID_COFFEE_NAMES

class NotEnoughResource(Exception):
    pass

class CoffeeMachine:
    def __init__(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    def create_coffee(self, coffee_name, amount):
        water_required = 0
        milk_required = 0
        coffee_required = 0
        cost = 0

        if coffee_name == "latte":
            water_required = 100
            milk_required = 50
            coffee_required = 50
            cost = 25
        elif coffee_name == "cappuccino":
            water_required = 200
            milk_required = 150
            coffee_required = 150
            cost = 35
        elif coffee_name == "espresso":
            water_required = 350
            milk_required = 300
            coffee_required = 250
            cost = 45

        if self.water < water_required:
            raise NotEnoughResource(f"Not enough water. We are returning the amount you gave us:{amount}")
        elif self.milk < milk_required:
            raise NotEnoughResource(f"Not enough milk. We are returning the amount you gave us:{amount}")
        elif self.coffee < coffee_required:
            raise NotEnoughResource(f"Not enough coffee. We are returning the amount you gave us:{amount}")

        self.water -= water_required
        self.milk -= milk_required
        self.coffee -= coffee_required

        return f"{coffee_name} total coffee made cost: {cost}", f"Your change is: {amount - cost}"

def get_valid_note_input():
    while True:
        note = input("Please insert a note we have accepted notes only [5, 10, 20, 50] or enter 'done' to finish: ")
        if note.lower() == 'done':
            return None
        try:
            note = int(note)
            if is_valid_note(note):
                return note
            else:
                print("Invalid note. Please enter a valid note.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")

def main():
    coffee_name = input("Which coffee would you like? (latte, cappuccino, espresso): ")
    while not is_valid_coffee_name(coffee_name):
        print("You entered an invalid coffee name. Please enter a valid coffee name.")
        coffee_name = input("Which coffee would you like? (latte, cappuccino, espresso): ")

    total_amount = 0
    while True:
        note = get_valid_note_input()
        if note is None:
            break
        total_amount += note

    coffee_machine = CoffeeMachine(500, 500, 200, 0)
    try:
        cost, change = coffee_machine.create_coffee(coffee_name, total_amount)
        print(cost, change)
    except NotEnoughResource as e:
        print(e)

if __name__ == "__main__":
    main()
