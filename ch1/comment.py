# 주석
"""
여러 줄 주석 처리
"""
'''
여러 줄 주석 처리
'''

# 화면출력 - print() / 변수타입 확인 - type()
print("Hello Python!!!")
print("100")
print(25.3)
print(type(100))    # <class 'int'>
print(type("100"))  # <class 'str'>
print(type(100.15)) # <class 'float'>
print(type(True))   # <class 'bool'>  * True에서 T가 대문자

# sep : 문자열 사이 구분자(기본값 spacebar)
print('t','e','s','t')
print('t','e','s','t',sep='')
print('t','e','s','t',sep='-')

# end : 기본값은 엔터, 줄 바꾸지 않고 그대로 이어서 써짐
print("welcome To", end=' ')
print("the black prade=")

# format : %s(문자열,정수,실수), %d(정수), %f(실수), %c(문자열 하나)
print("%d" % 100)
print("%5d" % 100)  # 5자리 맞춰서 출력
print("%05d" % 100) # 5자리 맞춰서 출력(자릿수 없는 것은 0으로 채움)
print()
print("%s" % "hi")
print("%5s" % "hi")
print()
print("%-8.2f" % 123.21) # 전체자릿수는 8자리 소수점자리는 2자리 -를 붙이면 왼쪽정렬
print("%8.2f" % 123.21)
print("%8.2f" % 123.213456)

# 변수 선언(타입 선언 안함 - 값에 따라 타입 결정)
number = 3
print("I eat %d apples" % number)
print("I eat", number, "apples")

print("%d : %s" % (1, "홍길동")) # 대입하는 값이 여러개이면 괄호()로 묶어줘야 함

# %s 는 타입이 디테일하게 정해져있지 않다면 어느타입이든지 쓸 수 있음
print("I eat %s apples" % 2)
print("I eat %s apples" % 3.156)
print("I eat %s apples" % "two")

# 98% (%를 한번 더 입력)
print("Error is %d%%" % 98)

# format() 함수
print("\nformat 함수 : {}")
print("{} and {}" .format("You","Me")) # You and Me
print("I eat {} apples" .format(3)) # I eat 3 apples
print("I eat {0} apples" .format(3)) 
print("{0} and {1} and {0}" .format("You","Me")) # 중괄호안에 숫자는 인덱스를 의미 You and Me and You
print("{var1} and {var2}" .format(var1="You",var2="Me")) # 중괄호안에 숫자는 변수를 의미 You and Me
print("{0} and {var2}" .format("You",var2="Me")) # 변수와 인덱스를 혼합의 형태로도 쓸 수 있음 You and Me

# 이스케이프 문자 : \n, \t
print("\n줄바꿈\n연습")
print("\\ 역슬래쉬") # 역슬래쉬를 쓰려면 두번 써야함
print(r"\n \t \\ 그대로 출력")
print("글자가 '강조'되는 효과") # 문자 표현시 "", '' 허용
print('글자가 "강조"되는 효과') # 문자 표현시 "", '' 허용















