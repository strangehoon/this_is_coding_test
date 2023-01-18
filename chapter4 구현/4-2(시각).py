N = int(input())

total_case = (N+1)*6*10*6*10

if N < 3:
    result = total_case - (N+1)*5*9*5*9
elif 3 <= N < 13:
    result = total_case - (N)*5*9*5*9
elif 13<= N < 23:
    result = total_case - (N-1)*5*9*5*9
else:
    result = total_case - (N-2)*5*9*5*9

print(result)
