data = input()

list_alpa = []
sum = 0

for x in data:
    # isalpha() 함수 쓰는게 더 좋았을 듯
    if 65<=ord(x)<= 90:
        list_alpa.append(x)
    else:
        sum += int(x)

list_alpa.sort()

# join함수를 써서 리스트를 문자열로 반환
alpha = ''.join(list_alpa)
if sum != 0:
    result = alpha + str(sum)

print(result)