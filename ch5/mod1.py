def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# 모듈 함수 확인용
# __name__는 mod1 직접 실행하게 되면 __main__ 이름을 가지게 됨
#           외부에서 mod1 실행시 mod1 이름을 가지게 됨
if __name__ == "__main__":
    print(add(3, 4))
    print(sub(8, 4))
