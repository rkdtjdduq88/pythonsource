# 파이썬 자료형
# 2. 리스트 (자바 배열, List 같은 개념)
# []

# 리스트 생성 - 데이터는 아무거나 가능(타입을 안맞춰도 괜춘)
list1 = []
list2 = ["a",1,3.15,True]
print(list1)
print(list2)
list3 = ["a",1,3.15,True,["b", 35, 45]]
print(list3) 

# 리스트 인덱싱
print(list2[0])
print(list2[2])
print(list2[-1])
print(list3[-1])
print(list3[-1][1])

# 리스트 슬라이싱
print(list2[0:2])
print(list3[:-1])
print(list3[4:]) #  [['b', 35, 45]]
print(list3[4]) #  ['b', 35, 45]
print(list3[4][:2]) # ['b', 35]

list4 = [1,2,["a","b",["Life","is"]]]
# is 문자열
print(list4[2][2][1])
print(list4[-1][-1][-1])

# + : 연결
a = [1,2,3]
b = [4,5,6]
print(a + b) # [1, 2, 3, 4, 5, 6]
print(a[0] + b[1]) # 6

# * : 반복
print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]


# 리스트 특정 요소 수정
a[1] = 7 
print(a) # [1, 7, 3]

a[2] = "Life"
print(a) # [1, 7, 'Life']

b[1:2] = [10,11] 
print(b) # [4, 10, 11, 6]

b[1] = [15,16,17]
print(b) # [4, [15, 16, 17], 11, 6]


# 리스트 요소 삭제
del b[1]
print(b) # [4, 11, 6]

b[0:1] = []
print(b) # [11, 6]

numbers = [273,103,5,32,65,9,72,800,99]
for number in numbers:
    if number >= 100:
        print("100 이상의 수 ", number)

# 273은 3 자릿수입니다.
# 103은 3 자릿수입니다.
# 5는 1자릿수입니다.
for number in numbers:
    print("{}는 {} 자릿수입니다.".format(number, len(str(number))))

# () : 튜플
list4 = list([1, 2, 3])
print(list4) # [1, 2, 3]

# 리스트 함수
# append() : 리스트 뒤에 요소 추가
list4.append(5)
print(list4) # [1, 2, 3, 5]
list4.append([6,7,8]) # [1, 2, 3, 5, [6, 7, 8]]
print(list4)

# sort()
print("정렬 전 ", numbers)
numbers.sort()
print("정렬 후 ", numbers)

alpha = ["a","z","c","b","f"]
alpha.sort()
print("정렬 후",alpha)

alpha = ["a","z","A","b","D","f"]
alpha.sort()
print("정렬 후 ", alpha)

han = ["고양이","강아지","원숭이","호랑이"]
han.sort()
print("정렬 후 ", han)

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
numbers.sort(reverse=True) # 내림차순 정렬
print("정렬 후",numbers) # [800, 273, 103, 99, 72, 65, 32, 9, 5]

# reverse() : 리스트 뒤집기
han.reverse() # ['강아지', '고양이', '원숭이', '호랑이']
print("reverse 후 ", han) # ['호랑이', '원숭이', '고양이', '강아지']

# index(찾고자하는 요소) : 요소가 존재하면 위치 반환

print(han[0])
print(han.index("호랑이"))
# print(han.index("악어"))  ValueError: '악어' is not in list

# insert(위치, 요소)
han.insert(1, "악어")
print("insert 후 ", han)  # ['호랑이', '악어', '원숭이', '고양이', '강아지']

# remove(삭제할 요소) :
# list = [1,3,3,5] ==> list.remove(3) : 첫 번째 찾은 3 만 제거해줌
han.remove("고양이")
print("remove 후 ", han) # ['호랑이', '악어', '원숭이', '강아지']

# pop() : 리스트 요소 중 마지막 요소 꺼내기
item = han.pop()
print("pop 대상 ", item)
han.pop()
print("pop 후 ", han) # ['호랑이', '악어', '원숭이']
han.pop(1)
print("pop 후 ", han) # ['호랑이', '원숭이']

# count()
a = [1, 2, 3, 1]
print("리스트에 포함된 1의 개수 ", a.count(1))

# clear() : 리스트 요소 모두 삭제
a.clear()
print("clear 후 ", a)

# 리스트 안의 요소가 비어 있는 경우 False 임
list1 = []
if list:
    print("True")
else:
    print("False")

# 문자열 안의 요소가 비어 있는 경우 False 임
str = ""
if str:
    print("True")
else:
    print("False")

# in
print("p" in "python")

fruits = ["사과", "딸기", "배", "자몽"]
print("사과" in fruits)
print("메론" not in fruits)

# 리스트 출력
for fruit in fruits:
    print(fruit)

print()

# enumerate() : index 부여
for fruit in enumerate(fruits):
    print(fruit) # (0, '사과')

print()

for idx,fruit in enumerate(fruits, start=1):
    print(idx,fruit) # 1 사과(start가 1이기 때문)

# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# 70, 60, 55, 75, 95, 90 , 80, 85, 100, 88
# 중간고사 점수를 리스트로 생성하고, A 학급의 평균 구하기
a_class = [70, 60, 55, 75, 95, 90 , 80, 85, 100, 88]

total = 0
for num in a_class:
    total += num
    
print("A 학급 평균 : %.2f" % (total / len(a_class)))

# sum() 이용
print("A 학급 평균 : %.2f" % (sum(a_class) / len(a_class)))

# 1 ~ 20 리스트 생성 : [1, 2, 3, 4...]
list2 = list(range(1,21))
print(list2)

list3 = []
for x in range(1,101):
    list3.append(x)
print(list3)

# comprehension
list3 = [x for x in range(1,101)]
print(list3)

print()

list4 = ["갑", "을", "병", "정", "경"]
# 정을 제외하고 출력
for x in list4:
    if x != "정":
        print(x)

# comprehension
list5 = [x for x in list4 if x != "정"]
print(list5)

# 1~100 숫자 중에서 홀수만 리스트로 생성
list6 = list(range(1,101,2))
print(list6)
list7 = []
for i in range(1, 101, 2):
    list7.append(i)
print(list7)
list8 = [i for i in range(1,101,2)]
print(list8)
list9 = [i for i in range(1,101) if i%2 == 1]
print(list9)

# 아래의 리스트에서 소문자만 추출해서 새로운 리스트로 생성
list10 = ["A","b","c","D","e","F","G","h"]
list11 = []
for x in list10:
    if x.islower():
        list11.append(x)

print(list11)

# list comprehension
list11 = [x for x in list10 if x.islower()]
print(list11)

# [1,2,3,4] ==> [2,4,6,8]
print([x * 2 for x in [1,2,3,4]])

# [0,1,2,3,4] ==> [0,1,4,9,16]
print([x * x for x in [0,1,2,3,4]])

# [1,2,3]
# [[1,2,3], [2,3,4], [3,4,5]]
list12 = [1,2,3]
list13 = []
for x in list12:
    list13.append([x,x+1,x+2])
print(list13)

print([[x,x+1,x+2] for x in list12])
    