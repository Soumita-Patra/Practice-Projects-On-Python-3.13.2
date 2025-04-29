# Print Price List in OOP


class Price_List():
    grade_list = ['grade1', 'grade2', 'grade3']

    def __init__(self):
        self.item_dic = {}

    def read_item_info(self):
        add_item = 'y'
        while add_item.lower() == 'y':
            try:
                items = input(f"Enter Item Name: ").strip().upper()
                print()
                try:
                    grade1_price = int(input(f"Enter 'Grade1' price for: {items}: "))
                    grade2_price = int(input(f"Enter 'Grade2' price for: {items}: "))
                    grade3_price = int(input(f"Enter 'Grade3' price for: {items}: "))
                    print()
                except ValueError:
                    print(f"Only Digits are Accapted!")
                    self.item_dic[items] = {
                            Price_List.grade_list[0] : grade1_price,
                            Price_List.grade_list[1] : grade2_price,
                            Price_List.grade_list[2] : grade3_price
                    }
                add_item = input(f"Type 'y' to Add Item or Type 'n': ")
                print()
            except ValueError:
                print(f"Invalid Input: Digits are not Accapted!")
        # print(self.item_dic)


    def calc_item_avg_amt(self):
        for key, val in self.item_dic.items():
            item_avg_amt = sum(list(val.values())) / len(val)
            self.item_dic[key].update({'avg_amt' : item_avg_amt})

    
    def print_price_list(self):
        line_length = '-' * 90
        print()
        print(line_length)
        print(f"Item \t\t Grade1 \t Grade2 \t Grade3 \t Avg.Price")
        print(line_length)
        for key, val in self.item_dic.items():
            print(f"{key} \t\t {val['grade1']} \t\t {val['grade2']} \t\t {val['grade3']} \t\t {val['avg_amt']:.2f}")
        print(line_length)
        print()



c1 = Price_List()
c1.read_item_info()
c1.calc_item_avg_amt()
c1.print_price_list()





# c1 = Price_List()
# c1.read_item_info()
































































































































































































































