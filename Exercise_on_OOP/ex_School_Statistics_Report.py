# School Statistics Report in OOP



class School_Strength():

    def __init__(self):
        self.klass_strength = {}
        self.boys_strength = {}
        self.girls_strength = {}

    def read_klass_info(self):
        add_klass = 'y'
        while add_klass.lower() == 'y':
            klass = int(input(f"Enter Class Number: "))
            boys_nunmer = int(input(f"Number of Boys: "))
            girls_number = int(input(f"Number of Girls: "))
            self.boys_strength[klass] = boys_nunmer
            self.girls_strength[klass] = girls_number
            add_klass = input(f"Type 'y' to Add Class or Type 'n' to Finish: ")
        # return self.boys_strength, self.girls_strength     # [Don't Need when 'self' is here in OOP]
    
    def calc_total_boys_in_school(self):
        self.total_boys = sum(list(self.boys_strength.values()))
        # return self.total_boys                             # [Don't Need when 'self' is here in OOP]
    
    def calc_total_girls_in_school(self):
        self.total_girls = sum(list(self.girls_strength.values()))
        # return self.total_girls                            # [Don't Need when 'self' is here in OOP]
    
    def calc_total_strength_in_klass(self):
        for key, val in self.boys_strength.items():
            self.klass_strength[key] = self.girls_strength[key] + self.boys_strength[key]
            self.total_strength_in_klass = sum(list(self.klass_strength.values()))
        # return self.total_strength_in_klass                # [Don't Need when 'self' is here in OOP]
    
    def print_school_stat_report(self):
        line_length = '-' * 70
        print()
        print(line_length)
        print(f"{'School Statistics Report':^70}")
        print(line_length)
        print(f"ClassNo. \t No.of Boys \t No.of Girls \t Total Strength")
        print(line_length)
        for key, val in self.klass_strength.items():
            boy = self.boys_strength[key]
            girl = self.girls_strength[key]
            print(f"{key} \t\t   {boy} \t\t   {girl} \t\t     {val}")
        print(line_length)
        print(f"Totals:  \t  {self.total_boys} \t\t   {self.total_girls} \t\t     {self.total_strength_in_klass}")
        print(line_length)
        print()


c1 = School_Strength()
c1.read_klass_info()
c1.calc_total_boys_in_school()
c1.calc_total_girls_in_school()
c1.calc_total_strength_in_klass()
c1.print_school_stat_report()


















































































































































































































































































































