# Arnas Oonsadao, 633040233-2
"""
Lab 8 OOP (Part 2: Encapsulation, Inheritance, and Polymorphism) : Problem 4
"""
class ComEnStudent:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def __str__(self):
        #str(self.name) + " has taken these courses: " + str(self.courses)
        return f"{self.name} has taken these courses:{self.courses}"

    def take_courses(self, *courses):
        self.courses.extend(courses)


class CoEStudent(ComEnStudent):
    def __init__(self, name, courses):
        super(CoEStudent, self).__init__(name, courses)


class DMEStudent(ComEnStudent):
    def __init__(self, name, courses):
        #self.type = ''
        super(DMEStudent, self).__init__(name, courses)

    def __str__(self):
        return super(DMEStudent, self).__str__() + f'\n' + DMEStudent.get_content_type(self)

    def make_content_type(self, content):
        self.type_content = content

    def get_content_type(self):
        #" specialized in creating content type: " + str(self.type_content)
        return f'specialized in creating content type: {self.type_content}'


if __name__ == "__main__":
    com_students = []
    manee = CoEStudent('Manee', ['EN813701'])
    mana = DMEStudent('Mana', ['EN842004'])
    manee.take_courses('EN813702', 'EN811301', 'EN811302')
    mana.take_courses('EN842005')
    mana.make_content_type('Infographics')
    com_students.append(manee)
    com_students.append(mana)
    for com_student in com_students:
        com_student.take_courses('SC401206')
        print(com_student)