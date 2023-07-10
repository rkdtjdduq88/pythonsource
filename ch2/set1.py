# 파이썬 자료형
# 5. 집합
# set() : 자바의 Set 과 동일
# 중복을 허용하지 않음
# 순서가 없음(==> 인덱싱 사용 불가)

set1 = set()
set2 = set([1,12,13,14])
set3 = set([1,4,5,6,6,6])

print(set1)
print(set2)
print(set3) # {1, 4, 5, 6} 중복된 숫자는 제거

t1 = (1,3,5,7)
set4 = set(t1)
print(set4) # {1, 3, 5, 7} 중괄호라도 키,벨류 값이 아니기때문에 set구조임

dict1 = {"a":10,"b":20,"c":30}
set5 = set(dict1)
print(set5) # {'a', 'b', 'c'} 딕셔너리에서 set구조로 변환하면 키값만 가지고옴

str1 = "abcdefg"
print(set(str1)) # {'g', 'd', 'c', 'f', 'e', 'b', 'a'} 문자열에서 set구조로 변환, 순서가 없음

# 교집합, 합집합, 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print("교집합") 
print(s1 & s2) # {4, 5, 6}
print(s1.intersection(s2)) # {4, 5, 6}

print("합집합")
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("차집합")
print(s1-s2) # {1, 2, 3}
print(s1.difference(s2)) # {1, 2, 3}

#add() - 1개의 값만 추가
s1.add(9) 
print(s1) # {1, 2, 3, 4, 5, 6, 9}

# update() - 여러 개의 값 추가
s1.update([10,11,12])
print(s1) # {1, 2, 3, 4, 5, 6, 9, 10, 11, 12}

# removie() - 특정 값 제거
s1.remove(10)
print(s1) # {1, 2, 3, 4, 5, 6, 9, 11, 12}

