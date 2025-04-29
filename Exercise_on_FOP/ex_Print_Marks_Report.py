# Print Marks Report in FOP


marks_report = {}
student_info_dic = {}
all_subject = []
grade_A = 400
grade_B = 300
grade_C = 200



def read_student_info():
    name = input(f"Enter Name of the Student: ").strip().upper()
    klass = int(input(f"Enter Class Number: "))
    roll_num = int(input(f"Enter Roll Number: "))
    student_info_dic[name] = {
        'Class' : klass, 
        'Roll_num' : roll_num
        }
    print(student_info_dic)
    print()


def read_subject_info():
    klass_num = [student_info_dic[key]['Class'] for key in student_info_dic.keys()][0]
        # explanation in broader way:
        # klass = [student_info_dic[key]['Class'] for key in student_info_dic.keys()]
        # klass_num = klass[0]    # value of klass comes out as a list, So to retrieve
        # the first element, here indexing has used :- klass[0]
    number_of_subjects = int(input(f"Enter Number of Subject for class {klass_num}:-  "))
    for each_number in range(number_of_subjects):
        subjects = input(f"Enter Subject({each_number+1}):->  ").strip().upper()
        all_subject.append(subjects)
    print(all_subject)
    print()


def read_marks_info():
    for each_sub in all_subject:
        marks = int(input(f"Enter Marks in {each_sub}:-  "))
        marks_report[each_sub] = marks
    print(marks_report)
    print()


def calc_total_marks():
    total = sum(list(marks_report.values()))
    return total

def calc_avg_marks(total):
    avg_marks = total / len(all_subject)
    return avg_marks

def calc_grade(total):
    if total >= grade_A:
        print(f" 'A' ")
    elif total >= grade_B:
        print(f" 'B' ")
    elif total >= grade_C:
        print(f" 'C' ")
    else:
        print(f" 'None' ")


def calc_status(total):
    if total < grade_C:
        print(f" !..Fail..! ")
    else:
        print(f" !..Pass..! ")


def print_marks_report(total, avg_marks):
    line_length = '-' * 90
    print()
    print(line_length)
    print(f"{'Marks Report':^70}")
    print(line_length)
    for key, val in student_info_dic.items():
        print(f"Name: {key} \t\t ClassNo: {val['Class']} \t\t Roll No: {val['Roll_num']}")
    print(line_length)
    print(f"{'Subjects:':<10}",end="")
    for each_sub in all_subject:
        print(f"{each_sub:<15}", end="")
    print()
    print(line_length)
    print(f"{'Marks(%):':<10}", end="")
    for val in marks_report.values():
        print(f"{val:<16}", end="")
    print()
    print(line_length)
    print(f"Total Marks: {total} \t\t\t Avg.Marks(%): {avg_marks}")
    print(line_length)
    print(f"STATUS: {calc_status()} \t\t\t\t Grade: {calc_grade()}")
    print(line_length)
    print()

      
read_student_info()
read_subject_info()
read_marks_info()
all_total = calc_total_marks()
avg = calc_avg_marks(all_total)
calc_grade(all_total)
calc_status(all_total)
print_marks_report(all_total, avg)




















































































































































































































































