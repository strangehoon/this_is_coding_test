N = int(input())
guild_list = list(map(int, input().split()))
guild_set = set(guild_list)

dummy = 0

#그룹수
total = 0

# guild_set에서 공포도가 작은 모험가부터 그룹화 여부 체크, 그룹이 안된 모험가는 dummy
while(len(guild_set) != 0):
    min_x = min(guild_set)
    count = guild_list.count(min_x)
    total += (count+dummy)//min_x
    dummy = count + dummy - ((count+dummy)//min_x)*min_x
    guild_set.remove(min_x)

print(total)

