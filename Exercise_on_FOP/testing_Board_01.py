class ReportBase:
    subjects = ['BENGALI', 'ENGLISH', 'HISTORY', 'GEOGRAPHY', 'BIOLOGY', 'PHYSICS', 'MATHEMATICS', 'SANSKRIT']
    grade_A = 400
    grade_B = 300
    grade_C = 200

    def __init__(self):
        self.student_info = {}
        self.marks_info = {}
        self.total_marks = 0
        self.avg_marks = 0.0


class StudentInfo(ReportBase):
    def read_student_info(self):
        try:
            klass_num = int(input("Enter Class Number Between Class 7 to Class 10: "))
            if klass_num < 7 or klass_num > 10:
                print("Invalid class number. Please try again.")
                return
            self.student_name = input("Enter Student Name: ").strip()
            roll_num = int(input("Enter Roll Number: "))
            self.student_info[self.student_name] = {
                'Class': klass_num,
                'Roll_num': roll_num
            }
            print("Student Info:", self.student_info)
            print()
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


class MarksInfo(ReportBase):
    def read_student_marks_info(self):
        try:
            for subject in ReportBase.subjects:
                marks = int(input(f"Enter Marks for {subject}: "))
                if marks < 0 or marks > 100:
                    print("Marks should be between 0 and 100. Please try again.")
                    return
                self.marks_info[subject] = marks
            self.student_info[self.student_name]['Marks'] = self.marks_info
            print("Updated Student Info:", self.student_info)
            print()
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


class StudentReport(StudentInfo, MarksInfo):
    def calc_student_total_marks(self):
        self.total_marks = sum(self.marks_info.values())
        print(f"Total Marks: {self.total_marks}")

    def calc_student_avg_marks(self):
        self.avg_marks = self.total_marks / len(ReportBase.subjects)
        print(f"Average Marks: {self.avg_marks:.2f}")

    def calc_grade(self):
        if self.total_marks >= ReportBase.grade_A:
            grade = 'A'
        elif self.total_marks >= ReportBase.grade_B:
            grade = 'B'
        elif self.total_marks >= ReportBase.grade_C:
            grade = 'C'
        else:
            grade = 'NONE'
        print(f"Grade: {grade}")

    def calc_status(self):
        status = 'PASS' if self.total_marks >= ReportBase.grade_C else 'FAIL'
        print(f"Status: {status}")

    def add_entry(self):
        while True:
            choice = input("Type [1] to Add New Entry or [0] to Exit: ")
            if choice == '1':
                self.read_student_info()
                self.read_student_marks_info()
                self.calc_student_total_marks()
                self.calc_student_avg_marks()
                self.calc_grade()
                self.calc_status()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


# Create an instance of StudentReport and start adding entries

c1 = ReportBase()
c1 = StudentReport()
c1.add_entry()
