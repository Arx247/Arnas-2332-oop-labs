# Arnas Oonsadao, 633040233-2
"""
Lab 7 OOP (Part 1: Class and Object) : Problem 1
"""
class Teacher:
    # Initializer / Instance Attributes
    def __init__(self, name, office_no, research_work, *course_work):
        self.name = name
        self.office_no = office_no
        self.research_work = research_work
        self.course_work = course_work

    def print_office_no(self):
        print(f'{self.name} has the office at Rm. {self.office_no}')

    def print_research_work(self):
        print(f'{self.name} is doing research in these topics {self.research_work}')

    def print_courses_work(self):
        print(f'{self.name} teacher these courses {self.course_work}')


if __name__ == '__main__':
    manee = Teacher("Manee", "Rm. 4203", "Artificial Intelligence", "EN842004", "EN813701")
    mana = Teacher("Mana", "Rm. 4209", "Internet of Things", "EN842005", "EN813703")
    manee.print_office_no()
    manee.print_research_work()
    manee.print_courses_work()
    mana.print_office_no()
    mana.print_research_work()
    mana.print_courses_work()
