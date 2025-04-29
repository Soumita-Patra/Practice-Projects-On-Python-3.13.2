

# Printing Cash Bill in FOP

item_with_rate = {}

item_with_rate['Idly'] = 10.00
item_with_rate['Vada'] = 20.00
item_with_rate['Dosa'] = 40.00
item_with_rate['Tea'] = 10.00
item_with_rate['Coffe'] = 10.00


def read_item_info():
    ordered = {}
    new_item = "y"
    while new_item.lower() == "y":     # Allows 'y' or 'Y'
        item = input(f"Enter Item Name: ").strip().upper()     # Convert item name to uppercase
        if item in item_with_rate:
            try:
                num_item = int(input(f"Number of {item}: "))
                if num_item > 0:
                    ordered[item] = num_item
                else:
                    print(f"Psitive Value Only")
            except ValueError:
                print(f"Enter Number Only")
        else:
            print("!Not Available!")
        new_item = input(f"Type 'y' to Add item or Type 'n': ").strip().title()
    print(f"{ordered}")
    return ordered


def calc_amt(ordered):
    item_amt = {}
    all_total = 0
    for each_item, qty in ordered.items():
        if each_item in item_with_rate:
            each_item_amt = item_with_rate[each_item] * qty
            item_amt[each_item] = each_item_amt
            all_total += each_item_amt
            print(f"{each_item} : {each_item_amt}")
    return all_total, item_amt

def print_bill(ordered, item_amt, total):
    line_length = "-" * 60
    print(line_length)
    print(f"{'CASH BILL':^60}")
    print(line_length)
    print(f"ITEM \t\t NOs \t\t RATE \t\t AMT(Rs)")
    print(line_length)
    for item, qty in ordered.items():
        rate = item_with_rate[item]
        item_price = item_amt[item]
        print(f"{item} \t\t {rate} \t\t {qty} \t\t {item_price}")
    print(line_length)
    print(f"TOTAL AMOUNT: \t\t\t\t\t {total}")
    print(line_length)
    print(f"{'!Thank You! Visit Again...':^60}")
    print()


food = read_item_info()
total, amt = calc_amt(food)
print_bill(food, amt, total)