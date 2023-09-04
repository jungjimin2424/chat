# from urllib import request
# from bs4 import BeautifulSoup
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")

# def hello():
#     target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
#     soup = BeautifulSoup(target, "html.parser")
#     output = ""
#     for location in soup.select("location"):
#         output += "<h3>{}</h3>".format(location.select_one("city").string)
#         output += "날씨{}<br/>".format(location.select_one("wf").string)
#         output += "최저/최고 기온: {}/{}"\
#         .format(
#             location.select_one("tmn").string,
#             location.select_one("tmx").string
#         )
#         output += "<hr/>"
#     return output


# students = [
#     {"name": "윤인성", "Korean": 87, "math":98, "english":88, "science": 95},
#     {"name": "연하진", "Korean": 92, "math":98, "english":96, "science": 98},
#     {"name": "구지연", "Korean": 76, "math":96, "english":94, "science": 90},
#     {"name": "나선주", "Korean": 98, "math":92, "english":96, "science": 92},
#     {"name": "윤아린", "Korean": 95, "math":98, "english":98, "science": 98},
#     {"name": "윤명월", "Korean": 64, "math":88, "english":92, "science": 92},
# ]

# print("이름","총점", "평균", sep="\t")

# for student in students:
#     score_sum = student["Korean"] + student["math"] +\
#     student["english"] + student["science"]
#     score_average = score_sum / 4
#     print(student["name"],score_sum,score_average,sep="\t")

# class Student:
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
#     def get_sum(self):
#         return self.korean + self.math + self.english + self.science
    
#     def get_average(self):
#         return self.get_sum() / 4
#     def to_string(self):
#         return "{}\t{}\t{}".format(
#             self.name,
#             self.get_sum(),
#             self.get_average()
#         )
# students = [
#     Student("윤인성", 87, 98, 88, 95),
#     Student("연하진", 92, 98, 96, 98),
#     Student("구지연", 76, 96, 94, 90),
#     Student("나선주", 98, 92, 96, 92),
#     Student("윤아린", 95, 98, 98, 98),
#     Student("윤명월", 64, 88, 92, 92),
# ]

# for student in students:
#     print(student.to_string())

# class Human:
#     def __init__(self):
#         pass
# class Student(Human):
#     def __init__(self):
#         pass

# student = Student()

# print("isinstance(student,Human):",isinstance(Student,Human))
# print("type(student) == Human: ", type(student) == Human)

# class Student:
#     def study(self):
#         print("공부를 합니다.")

# class Teacher:
#     def teach(self):
#         print("학생을 가르칩니다.")

# classroom = [Student(), Student(), Teacher(), Student(), Student()]

# for person in classroom:
#     if isinstance(person, Student):
#         person.study()
#     elif isinstance(person, Teacher):
#         person.teach()

# class Test:
#     def __init__(self, name):
#         self.name = name
#         print("{} -  생성되었습니다.".format(self.name))
#     def __del__(self):
#         print("{} - 파괴되었습니다.".format(self.name))

# a =Test("A")
# b =Test("B")
# c =Test("C")

# import math

# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#     def get_circumference(self):
#         return 2 * math.pi * self.__radius
#     def get_area(self):
#         return math.pi * (self.__radius ** 2)
    
# circle = Circle(10)
# print("# 원의 둘레와 넓이를 구합니다.")
# print("원의 둘레:", circle.get_circumference())
# print("원의 넓이:", circle.get_area())
# print()

# class Parent:
#     def __init__(self):
#         self.value = "테스트"
#         print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
#     def test(self):
#         print("Parent 클래스의 test() 메소드입니다.")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")

# child = Child()
# child.test()
# print(child.value)

# class CustomException(Exception):
#     def __init(self, message, value):
#         Exception.__init__(self)
#         self.message = message
#         self.value = value
#     def __str__(self):
#         return self.message
    
#     def print(self):
#         print("##### 어류정보 #####")
#         print("메시지: ", self.message)
#         print("값: ", self.value)
# try:
#     raise CustomException("그냥", 273)
# except CustomException as e:
#     e.print()

# result1 = 0
# result2 = 0

# def adder1(num):
#     global result1
#     result1 += num
#     return result1
# def adder2(num):
#     global result2
#     result2 += num
#     return result2

# # adder1(1)
# # print(result1)
# # adder2(3)
# # print(result2)
# # adder1(5)
# # print(result1)
# # adder2(9)
# # print(result2)

# class Calculator:
#     def __init__(self):
#         self.result = 0
    
#     def adder(self, num):
#         self.result += num
#         return self.result
    
# cal1 = Calculator()
# cal2 = Calculator()

# cal1.adder(3)
# cal2.adder(3)
# cal1.adder(5)
# cal2.adder(7)

# print(cal1.result)
# print(cal2.result)

# class Service:
#     # def setname(self, name):
#         self.name = name
#     def sum(self, a,b):
#         result = a + b
#         print(f"{self.name}님 {a} + {b} = {a+b}입니다")

# pey = Service()
# pey.setname("홍길동")
# pey.sum(1,1)

# pal = Service()
# pal.setname("김홍균")
# pal.sum(3,5)


# j = Service()
# j.setname("김석진")
# j.sum(100,20)

# class FourCal:
#     def setdata(self,first,second):
#         self.first = first
#         self.second = second
#     def sum(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def ssubum(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result
# a = FourCal()
# print(type(a))
# a.setdata(4,2)

# print(a.first)
# print(a.second)

# class HousePark:
#     lastname = "박"
#     def setname(self,name):
#         self.fullname = self.lastname + name
#     def travel(self, where):
#         print(f"{self.fullname},{where}여행을 가다")
#     def love(self, other):
#         print(f"{self.fullname},{other.fullname} 사랑에 빠졌네")
#     def __add__(self, other):
#         print(f"{self.fullname},{other.fullname} 결혼했네")
#     def __sub__(self, other):
#         print(f"{self.fullname},{other.fullname}")
# class Housekim(HousePark):
#     lastname = "김"
#     def travel(self, where,day):
#         print(f"{self.fullname},{where}여행{day}일 가다")

# pey = HousePark("응용")
# juliet = Housekim("줄리엣")
# pey.love(juliet)
# pey + juliet

