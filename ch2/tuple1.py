# 파이썬 자료형
# 3. 튜플(리스트와 거의 유사함)
#       ()사용 / 수정 불가 / 읽기만 가능

t1 = 1, 2, 3
print(t1) # (1, 2, 3)

# 원소 개수가 하나라면 , 가 필요함
t2 = (1,)
print(t2)

t3 = (1,2,("Life", "is"))
print(t3)

# 요소 삭제
# del t1[0]  # TypeError: 'tuple' object doesn't support item deletion
# 요소 변경
#t1[0] = 5 # TypeError: 'tuple' object does not support item assignment

# 인덱싱 / 슬라이싱
print(t1[0])
print(t1[0:2])

# 함수 리턴 값 ==> 여러 개의 값이 가능함 ==> 튜플로 리턴

# 튜플 ==> 리스트
print(list(t1)) # [1, 2, 3]

# 리스트 ==> 튜플
list1 = [5, 6, 7]
print(tuple(list1)) # (5, 6, 7)