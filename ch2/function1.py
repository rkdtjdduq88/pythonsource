# 함수
# 함수?(자바스크립트,파이썬) 메소드? ==> 기능 정의
# 함수 : 단독으로 실행
# 메소드 : 클래스 내부에 선언, 객체 생성 후 실행

# 함수 정의
def hello():
    print("Hello")

# 함수 호출
hello()

def add(a, b):
    return a + b

print(add(3,4))

# 기본값 : n = 2 => 함수 호출 시 값이 넘어오지 않는다면 기본값을 2로 하겠음

def print_n_times(value, n=2):
    for i in range(n):
        print(i, value)

print_n_times("안녕하세요", 5)  # 0 안녕하세요 1 안녕하세요 2 안녕하세요 3 안녕하세요 4 안녕하세요
print_n_times("반갑습니다")  # 0 반갑습니다 1 반갑습니다

# 가변 파라메터 : 다양한 값을 호출하고 싶을때 *args(가변)
def add_many(*args):
    print(args)

add_many({"dessert": "macaroon", "wine": "merlot"}) # ({'dessert': 'macaroon', 'wine': 'merlot'},)
add_many("35","24","48") # ('35', '24', '48')
add_many(["A","B","C","D"]) # (['A', 'B', 'C', 'D'],)
add_many() # ()

def add_many2(*args):
    result = 0
    for i in args:
        result += i
    print("합계", result)

add_many2(1,2,3)
add_many2(1,2,3,4,5,6)
add_many2(1,2,3,4,5,6,7,8,9)

def sum_mul(choice, *args):
    if choice == "mul":
        result = 1
        for i in args:
            result *= i
    elif choice == "add":
        result = 0
        for i in args:
            result += i
    return result

# TypeError: sum_mul() missing 1 required keyword-only argument: 'choice'
mul_result = sum_mul("mul",1,2,3,4,5,6)
add_result = sum_mul("add",1,2,3,4,5,6)

print("덧셈", add_result)
print("곱셈", mul_result)

# **kwargs : 키워드 파라미터(key=value)
def args_func1(**kwargs):
    print(kwargs)

args_func1(name="park") # {'name': 'park'}
args_func1(name="park", age=12) # {'name': 'park', 'age': 12}
args_func1(name="park", age=12, title="python") # {'name': 'park', 'age': 12, 'title': 'python'}

# 일반, 기본 파라메터, 가변 파라메터, 키워드 파라메터
def example_mul(arg1, arg2=15, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10,20) # 10 20 () {}
example_mul(10) # 10 15 () {}
example_mul(10,20, "park","kim") # 10 20 ('park', 'kim') {}
example_mul(10,20, "park","kim", age=15, name="cho") # 10 20 ('park', 'kim') {'age': 15, 'name': 'cho'}

# 다중 리턴
def sum_and_mul(a,b):
    return a+b, a*b

print(sum_and_mul(5,6)) # (11, 30)

add1, sum1 = sum_and_mul(5,6)
print("덧셈", add1) # 덧셈 11
print("곱셈", sum1) # 곱셈 720

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return y1, y2, y3

r1, r2, r3 = func_mul(100)
print(r1,r2,r3) # 10000 20000 30000

def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return [y1, y2, y3]

r1, r2, r3 = func_mul2(100)
print(r1,r2,r3) # 10000 20000 30000

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다" % nick)

say_nick("바보")
say_nick("야호")

# 두 개의 인자와 연산자를 받아 사칙연산을 수행하는 함수 작성

# def four_rules(num1,num2,op):
#     if op == "+":
#         return num1 + num2
#     elif op == "-":
#         return num1 - num2
#     elif op == "*":
#         return num1 * num2
#     else:
#         return num1 // num2

# num1 = int(input("숫자 1 입력 "))
# num2 = int(input("숫자 2 입력 "))
# op = input("연산자(+,-,*,//) 입력 ")
# print("{} {} {} = {}".format(num1, op, num2, four_rules(num1,num2,op)))

import random

# random.randrange(1,46) : 1~45 까지의 임의의 수 리턴
print("임의의 수", random.randrange(1, 46))

# 1~45 까지의 임의의 수 리턴 함수 작성
# 6개의 숫자가 리스트에 담길 때까지 함수 호출
# 6개의 숫자가 담기면 함수 호출 종료 후 리스트 출력
list1 = []

def get_number():
    return random.randrange(1, 46)

while True:
    num = get_number()

    if list1.count(num) == 0: # 중복 숫자 제외
        list1.append(num)

    if len(list1) >= 6:
        break

list1.sort()
print(list1)

a = 1

# 파이썬 함수 내부에서는 외부에 선언한 변수를 사용할 수 없음
# 외부 변수 사용 시 global 키워드 필요
def func1():
    global a 
    a += 3 
    print(a) # UnboundLocalError  # global a 를 추가한 후 : 4

func1()

# 람다 함수
# def square(x):
#     return x * x

# print(square(5))

square = lambda x: x * x
print(square) # <function <lambda> at 0x000001C0E5769620>
print(square(5))

add = lambda a,b:a+b
print(add(5,6))

def str_len(s):
    return len(s)

strings = ["bob","charles","alexander","teddy"]
strings.sort(key=str_len)
print(strings) # ['bob', 'teddy', 'charles', 'alexander']

strings.sort(key=lambda s:len(s))
print(strings) # ['bob', 'teddy', 'charles', 'alexander']


even_list=[]

def even(arr):
    for n in arr:
        if n % 2 == 0:
            even_list.append(n)

even([1,2,3,6,8,9,10,12])
even(list1)
print(even_list)

# List comprehension
even_list2 = [n for n in list1 if n % 2 == 0]
print(even_list2)

# lambda + filter
def even2(n):
    return n % 2 == 0
print(list(filter(even2, list1)))
print(list(filter(lambda n: n % 2 == 0, list1)))

# lambda + map
def mul(x):
    return x**2

nums = [1,2,3,6,8,10,11,12,13,14,15]

# map(함수, 리스트)
print(list(map(mul, nums))) # [1, 4, 9, 36, 64, 100, 121, 144, 169, 196, 225]

print(list(map(lambda x: x**2, nums))) # [1, 4, 9, 36, 64, 100, 121, 144, 169, 196, 225]

nums = list(range(1, 11)) # 1 ~ 10 리스트 생성

# 3의 배수만 문자열로 변경한 새로운 리스트 반환 ==> str(3) ==> '3'
# [1,2,'3',4,5,'6',7,8,'9']
# def asd(x):
#     if x%3==0:
#         return str(x)
#     else:
#         return x
    
# print(list(map(asd, nums))) # [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

nums_result=[]

def str_check(nums):
    '''
    리스트 안의 요소가 3의 배수인 경우 문자로 반환
    '''
    for i in nums:
        if i % 3 == 0:
            nums_result.append(str(i))
        else:
            nums_result.append(i)

    return nums_result

print(str_check(nums)) # [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

# filter, map
def str_check2(i):
    if i % 3 == 0:
        return str(i)
    else:
        return i

print(list(map(str_check2,nums))) # [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

print(list(map(lambda i:str(i) if i % 3 == 0 else i, nums))) # [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

