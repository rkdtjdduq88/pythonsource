class UserInfo:
    """
    Author : Hong
    Date : 2023.06.21
    Description : 클래스 작성법 - 인자 있는 생성자(오버로딩 유사)
    """

    def __init__(self, name, age, email=None) -> None:
        self.name = name
        self.age = age
        self.email = email

    def user_info(self):
        return "name : {}, age : {}, email : {}".format(self.name, self.age, self.email)


# 객체 생성
user1 = UserInfo("홍길동", 30, "hong@naver.com")
user2 = UserInfo("김유신", 20)

# user_info 호출
print(user1.user_info())
print(user2.user_info())
