x = 1
if x > 0:
    a = 1
    b = 2
    c = a + b
else:
    a = -1
    b = -2
    c = a-b


print(c)
print('안녕')
####################################
import math
n = math.sqrt(9.0)
print(n)
####################################
import pandas
####################################

a=1.2
a=-3.45
print(a, type(a))

b=4.34E10
c=4.24e-10

print(c)
####################################
x = True
y = False

if x and y :
    print("yes")
####################################

a = [1, 2, 3, 4]
b= 3 in a
print(b)

####################################

print("""문자열
            길게
        사용""")

###################################
p = "이름: %s 나이: %d" % ("김유신", 65)
print(p)
###################################

a = ","
b = a.join('abcd')
print(b)

###################################

# 양쪽 공백 지우기 strip()
a = " hi "
b = a.strip()
print(b)

###################################
# 문자열 나누기 (split)
a = "Life is too short"
b = a.split()
print(b)

c="a:b:c:d"
d = a.split(":")
print(d)

###################################
"""a = input("문자를 입력하세요: ")
print(a)

number = input("숫자를 입력하세요: ")
print(number)

a = input("문자를 입력하세요: ")
print(a.split())
"""
###################################
#  "" + 동일함
print("life" "is" "too" "short")
print("life" + "is" +"too" +"short")

###################################

#특정 블럭/ 분장을 수행하지 않고 그냥 스킵하기 위해선 pass 키워드 사용
if x <10:
    pass

####################################

treeHit = 0
while treeHit <10 :
    treeHit +=1
    print("나무를 %d번 찍었습니다. " % treeHit)
    if treeHit == 10 :
        print("나무 넘어갑니당")

#####################################
test_list = ['one', 'tow', 'three']

for i in test_list:
    print(i , "", end='')

#####################################
marks = [90, 25, 67, 45, 80]
 # 아래에서 i는 key값 mark는 value 값
for i, mark in enumerate(marks):
    number = i+1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

#####################################
#len(s)은 입력값 s의 길이(요소의 전체 갯수)를 돌려주는 함수
for x in range (len(marks)):
    print(x, marks[x])

#####################################
a, b, c = "파이선 ^^ !!!".split()
print(a)
print(b)
print(c)

#####################################









