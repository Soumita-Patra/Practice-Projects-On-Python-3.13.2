# Print Marks Report in OOP


class Individual_Student_Marks_Report():
    subjects = ['BENGALI', 'ENGLISH', 'HISTORY', 'GEOGRAPHY', 'BIOLOGY', 'PHYSICS', 'MATHEMATICS', 'SANSKRIT']
    grade_A = 400
    grade_B = 300
    grade_C = 200


    def __init__(self):
        self.student_info = {}
        self.marks_info = {}



    def read_student_info(self):
        klass_num = int(input(f"Enter Class Number Between Class 7 to Class 10: "))
        self.student_name = input(f"Enter Student Name: ")
        roll_num = int(input(f"Enter Roll Number: "))
        self.student_info[self.student_name] = {
                'Class' : klass_num,
                'Roll_num' : roll_num
            }
        print(self.student_info)
        print()


    def read_student_marks_info(self):
        for each_sub in Individual_Student_Marks_Report.subjects:
            marks_of_subject = int(input(f"Enter Marks for {each_sub}:- "))
            self.marks_info[each_sub] = marks_of_subject
        self.student_info[self.student_name]['Marks'] = self.marks_info
        print(self.student_info)
        print()



    def calc_student_total_marks(self):
        self.total_marks = sum(list(self.marks_info.values()))

    def calc_student_avg_marks(self):
        self.avg_marks = self.total_marks / len(Individual_Student_Marks_Report.subjects)


    def calc_grade(self):
        if self.total_marks >= Individual_Student_Marks_Report.grade_A:
            print(f" 'A' ")
        elif self.total_marks >= Individual_Student_Marks_Report.grade_B:
            print(f" 'B' ")
        elif self.total_marks >= Individual_Student_Marks_Report.grade_C:
            print(f" 'C' ")
        else:
            print(f" 'NONE' ")


    def calc_status(self):
        if self.total_marks < Individual_Student_Marks_Report.grade_C:
            print(f"FAIL")
        else:
            print(f"PASS")



    def print_marks_report(self):
        line_length = '-' * 80
        print()
        print(line_length)
        print(f"{'Marks Report':^80}")
        print(line_length)
        for key in self.student_info.keys():
            print(f"Name: {key} \t\t ClassNo.: {self.student_info[key]['Class']} \t\t Roll No.: {self.student_info[key]['Roll_num']}")
        print(line_length)
        print(f"Subjects:", end="")
        marks_dic = self.student_info[self.student_name]['Marks']
        for key in marks_dic.keys():
            print(f"{key}", end="")
        print()
        print(line_length)
        print(f"Marks(%):", end="")
        for val in marks_dic.values():
            print(f"{val}", end="")
        print()
        print(line_length)
        print(f"Total Marks : {self.total_marks} \t\t\t\t Avg.Marks(%) : {self.avg_marks} ")
        print(line_length)
        print(f"STATUS: {self.calc_status()} \t\t\t\t Grade: {self.calc_grade()} ")
        print(line_length)
        print()
        print()



class Add_New_Entry(Individual_Student_Marks_Report):

    def add_entry(self):
        while True:
            add_entry = input(f"Type [1] to Add New Entry or Type [0]:-   ")
            print()
            print()
            if add_entry == '1':
                self.entry_info()
            elif add_entry == '0':
                print(f"Exiting")
                break
            else:
                print(f"Invalid Input")



    def entry_info(self):
        self.read_student_info()
        self.read_student_marks_info()
        self.calc_student_total_marks()
        self.calc_student_avg_marks()
        self.calc_grade()
        self.calc_status()
        self.print_marks_report()
        



c1 = Add_New_Entry()

c1.entry_info()
c1.add_entry()


    
            


































































































































































































































