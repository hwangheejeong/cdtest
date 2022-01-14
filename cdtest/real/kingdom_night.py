#구현
#왕실의 나이트

loc = input()
row = int(loc[1])
#ord 함수 : 하나의 문자를 넣으면 유니코드로 반환
col = int(ord(loc[0]))-int(ord('a'))+1

#8가지 방향정의 : L자로만 이동가능
steps =[(-2,1),(-2,-1),(2,-1),(2,1),(1,-2),(1,2),(-1,2),(-1,-2)]

#8가지 모두 이동가능한지 확인
result = 0
for s in steps:
    #현재 위치에 각 행과 열 이동 후 위치
    next_row = row+s[1]
    next_col = col+s[0]

    if next_row >=1 and next_row<=8 and next_col >=1 and next_col<=8 :
        result += 1

print(result)