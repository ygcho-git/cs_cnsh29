# 실습과제1 - tuple
T = (1, 2, 3, 3)

print(T) # (1, 2, 3, 3)

print(len(T)) # 4

print(T[1])   # 2
print(T[1:3]) # (2, 3)

T[1] = 20 # 불가
print(sum(T), max(T), min(T))  # 9, 3, 1

print(T.count(3))  # 2
print(T.index(2))  # 1

T = (1, 2) + (3, 4)  # (1, 2, 3, 4)
T = (1, 2) * 2       # (1, 2, 1, 2)


# 실습과제2 - set(순서가 없음)
S1 = {1, 2, 3, 4, 5, 5, 4} # 중복된 값이 있으면 자동 제거
S2 = {4, 5, 6, 7, 8}

print(S1)      # {1, 2, 3, 4, 5} 중복된 값은 제거됨.

print(len(S1)) # 5

print(S1[1]) # 순서가 없으므로 index로 접근 불가

print(S1 & S2)  # 교집합 {4, 5}                      s1.intersection(s2)
print(S1 | S2)  # 합집합 {1, 2, 3, 4, 5, 6, 7, 8}    s1.union(s2)
print(S1 - S2)  # 차집합 {1, 2, 3}                   s1.difference(s2)

S1.add(100)  # 값 1개 추가 {1, 2, 3, 4, 5, 100}
S1.update({200, 300}) # 값 2개이상 추가 {1, 2, 3, 4, 5, 100, 200, 300}
S1.remove(1) # 원소 중 2 제거 {2, 3, 4, 5, 100, 200, 300}

print(S1) # {2, 3, 4, 5, 100, 200, 300}


# 실습과제3 - dict(순서가 없음)
D = {"H":1.01, "He":4.00, "Li":6.94}

print(D)  # {'H': 1.01, 'He': 4.0, 'Li': 6.94}
print(len(D)) # 3

print(D[1]) # 순서가 없으므로 index로 접근 불가
print(D["H"]) # 1.01 혹은 get()메소드를 사용해 print(D.get("H"))

D["Be"] = 9.01  # "Be":9.01 쌍을 추가
del D["Li"]  # "Li":6.94 쌍을 삭제

print(D.items()) # dict_items([('H', 1.01), ('He', 4.0), ('Be', 9.01)])
print(D.keys()) # dict_keys(['H', 'He', 'Be'])
print(D.values()) # dict_values([1.01, 4.0, 9.01])
