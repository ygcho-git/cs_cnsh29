# 실습과제1 - 리턴값의 개수 - 파이썬은 리턴값의 개수를 2개 이상 쓸 수 있다. 
def func2() :
    return 1, 2

res = func2()
print(res)
print(res[0], res[1])



# 실습과제2 - 디폴트 매개변수
def introduce(name, age, school="충남과학고") :
    print("이름 :", name, "나이 :", age, "학교 :", school)

introduce("홍길동", 18, "율도고")  # 이름 : 홍길동 나이 : 18 학교 : 율도고
introduce("김도균", 17)            # 이름 : 김도균 나이 : 17 학교 : 충남과학고
introduce("김도균")                # 오류(age 값 없음)

introduce(17, "김도균")            # 이름 : 17 나이 : 김도균 학교 : 충남과학고 
introduce(age=17, name="김도균")   # 이름 : 김도균 나이 : 17 학교 : 충남과학고 


# 실습과제3 - 가변인자
# r1 = max(1, 2, 3)              
# r2 = max(1, 2, 3, 4, 5)
def func3(a, *b) :
   print(a, b)

func3(1, 2, 3)
