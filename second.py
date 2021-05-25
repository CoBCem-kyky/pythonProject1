# ООП

class Person:
    people_count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people_count += 1
        print("A'am Alive")

    def sey_hello(self):
        print(f"{self.name} says hello!")

class Student(Person):
    def study(self):
        print(f"{self.name} studies")

class Teacher(Person):
    def tech(self):
        print(f"{self.name} teaches")

s1 = Student("Name", 20)
t1 = Teacher("John", 35)

#t1.sey_hello()
#s1.sey_hello()

#s1.study()
#t1.tech()

def introduce(person):
    print("Sey HEllo")
    person.sey_hello()

people_arr = [Student("Tom", 18), Teacher("Katy",35), Student("Bob", 26)]
for person in people_arr:
    introduce(person)


# Домашняя работа
#Animal - name
#eat -{name} is eating
#Dog- доп. атрибут breed, bark()- "Dog name {name} is barking"
#Cat - доп. атрибутов нет, meow() - "Meow"
# Frog - доп. атрибутов нет, eat() - Frog is eating - переопределить метод eat