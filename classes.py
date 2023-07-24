from Student import Student

student1 = Student("John", "Accounting", 3.6, False)
student2 = Student("Jane", "Mathematics", 2.5, True)

print(student1.name)

# class functions
print(student1.on_honor_roll())
print(student2.on_honor_roll())
