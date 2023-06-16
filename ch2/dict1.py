# 파이썬 자료형
# 4. 딕셔너리 (자바의 Map 동일 : key, value)
# {} 사용

# key 값은 str, int 가능
# value 값은 str, int, list, tuple, dictionary
dict1 = {"name":"park", "age": 12}
print(dict1)

# 특정 키에 해당하는 value 출력
print(dict1["name"])
print(dict1["age"])
# print(dict1["addr"]) KeyError: 'addr'

dict2 = {0 : "Hello Python", 1 : "Hello Java"}
print(dict2)
print(dict2[0]) # Hello Python

dict3 = {"arr":[1,2,3,4]}
print(dict3)
print(dict3["arr"])

# 요소 추가
dict1["birth"] = "0616"
print(dict1)

dict2[2] = ["Hello Spring","Hello JSP"]
print(dict2)

dict3["rank"] = (16,17,18)
print(dict3)

# 각 숫자가 몇 개씩 나오는지 구한 후 딕셔너리 생성
# {1:3, 2:4, 6:1......}
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]

# 비어 있는 dict 생성
counter = {}

for number in numbers:
    counter[number] = numbers.count(number)
print(counter)

# 요소 삭제
del dict1["birth"]
print(dict1)

# 함수
# get(키값)
print(dict1.get("name"))
print(dict1.get("addr")) # None