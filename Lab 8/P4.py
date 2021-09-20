class ComEnStudent:
    name = []
    courses = []
    def __init__(self, *name, courses):
        self.name = name
        self.courses = courses

    def __str__(self):
        return str(self.name) + ' has taken these courses: ' + str(self.courses)

class CoEStudent:
    def __init__(self, *name, courses):
        self.name = name
        self.courses = courses

    def get_courses(self):
        return self.courses
    def take_courses(self, *courses):
        self.courses = courses




class DMEStudent:
    def __init__(self, name, courses, content):
        self.name = name
        self.courses = courses
        self.content = content

    def __str__(self):
        return 'Specialized in creating content type: ' + str(self.content)
    def get_courses(self):
        return self.courses and self.content

    def take_courses(self, *courses):
        self.courses = courses

    def make_content_type(self,content):
        self.content = content




if __name__ == "__main_.":
com_students = []
manee = CoEStudent ("Manee", ["EN813701"])
mana = DMEStudent("Mana", ["EN842004"])
manee.take_courses ("EN813702", "EN811301", "EN811302")
mana.take_courses ("EN842005")
mana.make_content_type("Infographics")
com_students.append(manee)
com_students.append(mana)
for com_student in com_students:
    com_student.take_courses ("SC401206")
    print(com_student)
