# dict_a = {
#     "name":"어밴저스 엔드게임",
#     "type":"히어로 무비"
# }

# print(dict_a)
# print(dict_a["name"])
# print(dict_a["type"])

# dict_b = {
#     "director":["안소니 루소","조 루소"],
#     "cast":["아이언맨","타노스","토르","닥터스트레인지","헐크"]
# }

# print(dict_b["director"])
# print(dict_b["cast"])

# dictionary = {
#     "name" : "70 건조 망고",
#     "type" : "당절임",
#     "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin": "필리핀"
# }

# print("name", dictionary["name"])
# print("type:", dictionary["type"])
# print("ingredient:", dictionary["ingredient"])
# print("origin:", dictionary["origin"])
# print()

# dictionary["name"] = "80 건조 망고"
# print("name:", dictionary["name"])

# import random
# print(random.randint(0, 2))
# import random
# numbers = []
# for i in range(6):
#     number = random.randint(1, 10)
#     if number not in numbers:
#         numbers.append(number)
# print(numbers)

# dictionary = {
#     "name" : "7D 건조 망고",
#     "type" : "당절임",
#     "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin": "필리핀"

# }

# key = input("> 접근하고자 하는 키:")

# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("존재하지 않는 키에 접근하고 있습니다.")

# value = dictionary.get("존재하지 않는 키")
# print("값:", value)

# if value == None:
#     print("존재하지 않는 키에 접근했었습니다.")

# for key in dictionary:
#     print(key, ":", dictionary[key])

# numbers = [1,2,6,8,3,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2]
# counter = {}
# for number in numbers:
#     if number in counter:
#         counter[number] += 1
#     else:
#         counter[number] = 1

# print(counter)

# for key in character:
#     if type(character[key]) is dict:
#         dicdic = character[key]
#         for k in dicdic:
#             print(k, ":", dicdic[k])
#     elif type(character[key]) is 

# array = [273, 32, 103, 57, 52]

# for i in range(len(array)):
#     print(f"{i}번째 반복 : {array[i]}")

# numbers = [5, 15, 6, 20, 7, 25]

# for number in numbers:
#     if number < 10:
#         continue
#     print(number)

# max_value=0
# a = 0
# b = 0

# for i in range(1,100 +1):
#     j = 100 -i

#     if i * j > max_value:
#         max_value = i * j
#         a = i
#         b = j

# print(a,b,max_value)

# example_list = ["요소A","요소B","요소C"]

# print("단순 출력")

# print(example_list)
# print()

# print("enumerate() 함수 적용 출력")
# print(enumerate(example_list))
# print()

# for i, value in enumerate(example_list):
#     print(f"{i}번째 요소는 {value}입니다.")

# example_dictionary = {
#     "키A" : "값A",
#     "키B" : "값B",
#     "키C" : "값C"
# }

# print("딕셔너리의 items() 함수")

# print(example_dictionary.items())
# print()

# for key, element in example_dictionary.items():
#     print(f"dictionary{key} = {element}")

# array = []


# for i in range(0, 20,2):
#     array.append(i * i)

# print(array)

# array = [i * i for i in range(0,20,2)]
# print(array)

# array =["사과","자두","초콜릿","바나나","체리"]
# output = []   
# for fruit in array:
#      if fruit != "초콜릿":
#         output.append(fruit)
# print(output)

# output = [fruit for fruit in array if fruit != "초콜릿"] 

# print(output)

# numbers = [1,2,3,4,5,6]

# r_num = reversed(numbers)
# print(r_num)

# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))
# print(next(r_num))

# i = 0
# for i in range(11):
#     i = i + 2
#     print(i * "*")

# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")

# print_3_times()

# def print_n_times(value,n):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요",5)

# def print_n_times(n, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

# def return_test():
#     return 100

# value = return_test()
# print(value)

# def sum_all(start=0, end=100, step=1):
#     output = 0
#     for i in range(start, end + 1,step):
#         output += i
#     return output

# print(f" 0 to 100 {sum_all(0,100,10)}")
# print(f" 0 to 1000 {sum_all(end=100)}")
# print(f" 50 to 100 {sum_all(end=100, step=2)}")


# def mul(*values):
#     output = 1
#     for v in values:
#         output *= v

#     return output
# print(mul(5,7,9,10))

# def function(*values, valueA, valueB):
#     pass

# function(1,2,3,4,5)

# file = open('basic.txt',"w")

# file.write("Hello Python Programming...!")

# file.close()

# with open("basic.txt", "r")as file:
#     contents = file.read()

# print(contents)

# import random
# hanguls = list("가나다라마바사아자차카타파하")
# with open("info.txt", "w")as file:
#     for i in range(1000):
#         name = random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40, 100)
#         height = random.randrange(140, 200)

#         file.write("{},{},{}\n".format(name,weight,height))

# with open("info.txt", "r") as file:
#     for line in file:
#         (name,weight,height) = line.strip().split(",")
#         if(not name) or (not weight) or (not height):
#             continue
#         bmi = int(weight)/((int(height)/100)**2)
#         result = ""
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상 체중"
#         else :
#             result = "저체중"

#         print('\n'.join([
#             "이름:{}",
#             "몸무게:{}",
#             "키:{}",
#             "BMI:{}",
#             "결과:{}"
#         ]).format(name, weight, height, bmi, result))
#         print()

# num = 0
# while num != 10:
#     num += 1
#     print(num)

# num = 10
# while num != 0:
#     print(num)
#     num -= 1    

# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee - 1
#     print(f"남은 커피의 양은 {coffee}개입니다.")
#     if not coffee:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# coffee = 10
# while True:
#     money=int(input("돈을 넣어주세요:"))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee - 1
#     elif money>300:
#         print(f"거스름돈 {money-300}을 주고 커피를 줍니다.")
#         coffee = coffee - 1
#     else:
#         print(f"돈을 다시 돌려준다 {money}")
#     if not coffee:
#         print("커피가 다 떨어졌다 판매중지")
#         break
#     print(f"남은 커피의 양 {coffee}")
# i = 0
# num = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         num = num + i
#     i = i + 1
# print(num)
# i = 0
# num = 0
# for i in range(10):
#     i += 1
#     num = num + i
# print(num)

# output = ""

# for i in range(1,11):
#     for j in range(10,i,-1):
#         output += ' '
#     for k in range(0,2 * i -1):
#         output += '*'
#     output += '\n'


# o = ""
# for a in range(9,0,-1):
#     for b in range(10,a,-1):
#         o += ' '
#     for c in range(0,2*a-1):
#         o += '*'
#     o += '\n'
# print(output,end='')
# print(o)

money = int(input("돈을 넣어주세요>"))

콜라 = 1200
우주맛콜라 = 1900
제로콜라 = 1200
스프라이트 = 1100
환타 = 900
닥터페퍼 = 1100
몬스터 = 1800
파워에이드 = 1900
네스티 = 1600
글라소비타민워터 = 2100
미닛메이드 = 1700
조지아커피 = 900
암바사 = 900
마테차 = 1700
