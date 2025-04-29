# Printing Cash Bill in OOP


class Food:
    # Menu with item rates
    item_with_rate = {
        'IDLY': 10.00,
        'VADA': 20.00,
        'DOSA': 40.00,
        'TEA': 10.00,
        'COFFEE': 10.00  
    }

    def __init__(self):
        # Initialize dictionaries for orders and calculated amounts
        self.ordered = {}
        self.amt = {}
        self.total = 0  # Initialize total amount

    def read_item_info(self):
        """Reads item information and quantities from the user."""
        new_item = 'y'
        while new_item.lower() == 'y':  # Allows 'y' or 'Y'
            item = input("Enter Item Name: ").strip().upper()  # Convert item name to uppercase
            # [Using self.item unnecessarily as an instance attribute 
            # when it is only used locally within read_item_info.]
            if item in Food.item_with_rate:
                try:
                    num_item = int(input("Number Of Items: "))
                # [Using self.num_item unnecessarily as an instance attribute
                # when it is only used locally within read_item_info.]
                    if num_item > 0:
                        self.ordered[item] = num_item  # Add valid item and quantity to the dictionary
                    else:
                        print("Invalid Input: Enter a positive number.")
                except ValueError:
                    print("Invalid Input: Please enter a valid number.")
            else:
                print("!Not Available!")
            new_item = input("Type 'y' to Add Item or Type 'n' to Finish: ").strip()
        return self.ordered

    def calc_amt(self):
        """Calculates the total amount and individual item amounts."""
        self.total = 0  # Reset total amount
        for item, qty in self.ordered.items():
            each_item_amt = Food.item_with_rate[item] * qty
            # [Using self.each_item_amt unnecessarily as an instance attribute 
            # when it is only used locally within calc_amt.]
            self.amt[item] = each_item_amt  # Store calculated amount for the item
            self.total += each_item_amt  # Add to total amount
        return self.total, self.amt

    def print_bill(self):
        """Prints the final bill in a formatted layout."""
        line_length = "-" * 60
        print()
        print(line_length)
        print(f"{'CASH BILL':^60}")
        print(line_length)
        print(f"ITEM \t\t NOs \t\t RATE \t\t AMT(Rs)")
        print(line_length)
        for item, qty in self.ordered.items():
            rate = Food.item_with_rate[item]
            price = self.amt[item]
            print(f"{item} \t\t {qty} \t\t {rate} \t\t {price}")
        print(line_length)
        print(f"TOTAL(Rs.) : \t\t\t\t {self.total}")
        print(line_length)
        print(f"{'!THANK YOU!..Visit Again':^60}")
        print()

# Execution
c1 = Food()
order = c1.read_item_info()
total, item_amt = c1.calc_amt()
c1.print_bill()



















































































































































































































































