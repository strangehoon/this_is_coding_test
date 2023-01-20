S = input()

list_0 = []
list_1 = []

# 임시 저장소 trans
trans = []
for i in range(len(S)):
    data = S[i]
    # trans가 비어있으면 뽑은 문자를 저장
    if len(trans) == 0:
        trans.append(data)
    else:
        # trans의 문자와 뽑은 문자가 다르면 trans에 저장되어 있는 값을 list_0 or list_1에 저장 후 trans를 reset
        if data =='1' and trans[0] == '0':
            result = ''.join(trans)
            list_0.append(result)
            trans.clear()
            trans.append(data)
        elif data == '0' and trans[0] == '1':
            result = ''.join(trans)
            list_1.append(result)
            trans.clear()
            trans.append(data)

        # 값이 같으면 trans의 문자열에 붙임
        else:
            trans.append(data)

# trans에 남아있는 데이터 비우기
result = ''.join(trans)
if result[0] == '0':
    list_0.append(result)
else:
    list_1.append(result)

# 최소 횟수 출력
if len(list_0) > len(list_1):
    print(len(list_1))
else:
    print(len(list_0))


