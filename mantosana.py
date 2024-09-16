class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('Person created')

    def say_helo(self):
        print(f'{self.name} says Hello!')

class Student(Person):
    def __init__(self,name,age,average_grade):
        super.__init__(name,age)
        self.average_grade=average_grade
        print('Student created')
    def study(self):
        print(f'{self.name} studies')
    def say_helo(self):
        print(f'Student with name: {self.name} says Hello!')    

class Teacher(Person):
    def teach(self):
        print(f'{self.name} teaches')

def introduce(person):
    print('Now a person will say hello')
    person.say_hello()

people_arr=[Student('tom', 15,4.5), Teacher('Katy', 37), Student('Bob, 26, 4.8')]

for person in range people_arr:
    introduce(person)

p1=Student('Tom', 15)
t1=Teacher('Katy', 37)
p1.say_hello()      
t1.say_hello()
p1.study()    
t1.teach()       