def student(name, age, gpa, is_on_probation):
    print("my name is " + name)
    print("my age is " + str(age))
    print("my gpa is " + str(gpa))
    if is_on_probation:
        print("i am on probation\n")
    else:
        print("i am not on probation\n")


def merit_student(self):
    print("start of merit_student function")
    if int(self.gpa) >= 2.5:
        print("This student is on merit list")
        return True

    else:
        print("This student is NOT on merit list")
        return False


'''
    def __init__(self, name, age, gpa, is_on_probation):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def print():
       print("hello world")
         

'''


class Teacher:
    def __init__(self, name, age, salary, will_get_fired):
        self.name = name
        self.age = age
        self.salary = salary
        self.will_get_fired = will_get_fired

    def print(self):
        print(" your name is " + self.name + "\n your age is " + str(self.age) + "\n your salary is " + str(self.salary))

    def fired(self):
        if self.will_get_fired:
            print("You will get fired")

        else:
            print("Your performance is good, keep it up")
