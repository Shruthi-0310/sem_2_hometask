#1
s_name=input("Enter the student name:")
s_rollno=int(input("Enter the Roll No.:"))
a=int(input("Enter the marks obtained in subject 1:"))
b=int(input("Enter the marks obtained in subject 2:"))
c=int(input("Enter the marks obtained in subject 3:"))
d=int(input("Enter the marks obtained in subject 4:"))
e=int(input("Enter the marks obtained in subject 5:"))
tot=a+b+c+d+e
per=(tot/500)*100
if per>=85:
    print("Grade S")
elif per>=75:
    print("Grade A")
elif per>=65:
    print("Grade B")
elif per>=55:
    print("Grade C")
elif per>=50:
    print("Grade D")
else:
    print("Grade E")


#1 with class

class student:
    def __init__(self,name,rollno,dep,sub1,sub2,sub3):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.per=((sub1+sub2+sub3)/3)*100
    def grade(self):
        if self.per>=80:
            print("Grade A")
        elif self.per>=60:
            print("Grade B")
        elif self.per>=40:
            print("Grade C")
        else:
            print("Grade D")
s=student("SHRUTHI N",E24AI045,"AI",100,100,100)
s.grade()

#2
class Student:
    def __init__(self,name,age,course,grade):#Self-Current instance of a class
        self.name=name
        self.age=age
        self.course=course
        self.grade=grade
    def show(self):
        print(f"student Details-Student Name {self.name},Student Age {self.age},Student Course {self.course},Student Grade {self.grade}")
    def __del__(self):
        print("ALL DETAILS ARE DELETED")
stu1=Student("HAKUNAMATATA",18,"AI","A")
stu1.show()
del stu1


