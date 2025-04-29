
# School Statistics Report in FOP

# school_strength = {}
klass_strength = {}


def read_klass_info():
    boy_strength = {}
    girl_strength = {}
    add_klass = 'y'
    while add_klass.lower() == 'y':
        klass = int(input(f"Enter Class Number: "))
        num_boy = int(input(f"Enter Number of Boys: "))
        num_girl = int(input(f"Enter Number of Girls: "))
        boy_strength[klass] = num_boy
        girl_strength[klass] = num_girl
        add_klass = input("Type 'y' to Add CLASS or Type 'n' to Finish: ").strip()
    return boy_strength, girl_strength

def calc_total_boy_strength(boy_strength):
    total_boys = sum(list(boy_strength.values()))
    return total_boys

def calc_total_girl_strength(girl_strength):
    total_girls = sum(list(girl_strength.values()))
    return total_girls

def total_strength_in_klass(boy_strength, girl_strength):
    for key, val in boy_strength.items():
        total_in_klass = girl_strength[key] + boy_strength[key]
        klass_strength[key] = total_in_klass
    return total_in_klass

def print_school_statistics_report(boy_strength, girl_strength, total_boys, total_girls, total_in_klass):
    line_length = "-" * 60
    print()
    print(line_length)
    print(f"{'School Statistics Report':^60}")
    print(line_length)
    print(f"ClassNo. \t\t No.of Boys \t\t No.of Girls \t\t Total Strength")
    print(line_length)
    for key, val in klass_strength.items():
        boy = boy_strength[key]
        girl = girl_strength[key]
        print(f"{key} \t\t {boy} \t\t {girl} \t\t {val}")
    print(line_length)
    total_strength = total_boys + total_girls
    print(f"Totals: \t\t {total_boys} \t\t {total_girls} \t\t {total_strength}")
    print(line_length)
    print()

boy_dic, girl_dic = read_klass_info()
all_boy = calc_total_boy_strength(boy_dic)
all_girl = calc_total_girl_strength(girl_dic)
all_student = total_strength_in_klass(boy_dic, girl_dic)
print_school_statistics_report(boy_dic, girl_dic, all_boy, all_girl, all_student)



