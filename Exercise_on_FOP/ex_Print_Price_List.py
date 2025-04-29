
# Print Price List in FOP

items_list = ['AAA', 'BBB', 'CCC']
grade = {}

def read_item_info():
    for each_item in items_list:
        grade1_price = int(input(f"Enter Grade1 Price for {each_item}: "))
        grade2_price = int(input(f"Enter Grade2 Price for {each_item}: "))
        grade3_price = int(input(f"Enter Grade3 Price for {each_item}: "))
        print()
        grade[each_item] = {
                            'grade1' : grade1_price,
                            'grade2' : grade2_price,
                            'grade3' : grade3_price
                        }
    # print(grade)

def calc_item_avg_amt():
    for key, val in grade.items():
        item_avg_amt = sum(list(val.values())) / len(val)
        grade[key].update({'avg_amt' : item_avg_amt})
    # print(grade)

  

def print_price_list():
    line_length = '-' * 70
    print()
    print(line_length)
    print(f"Item \t\t Grade1 \t Grade2 \t Grade3 \t Avg.Price")
    print(line_length)
    for key, val in grade.items():
        print(f"{key} \t\t {val['grade1']} \t\t {val['grade2']} \t\t {val['grade3']} \t\t {val['avg_amt']:.2f}")
    print(line_length)
    print()


read_item_info()
calc_item_avg_amt()
print_price_list()





































































































































































































































































