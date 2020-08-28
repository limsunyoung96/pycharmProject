"""
지금까지 배운 내용을 가지고
숫자와 문자를 입력받아 입력받은 문자열은 공백으로 자른다.

~ 10
    hellohellohello 입력 수만큼 붙여서 출력
10 ~ 99
    hello hello hello 입력 수만큼 입력받은 텍스트 출력(공백으로 띄우기
100 ~
    hello,hello,hello 입력 수만큼 입력 받은 텍스트 출력(,)

"""
inputStr = input("숫자와 문자를 입력하세요(공백).")
num, str = inputStr.split()
num = int(num)
strPint = ""
if num < 10:
    print(str * num)
elif 10 <= num < 100:
    for i in range(num):
        print(str, end=',')
else:
    for i in range(num):
        print(str, end='')
