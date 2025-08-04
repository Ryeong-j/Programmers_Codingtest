# # UTF-8 encoding when using korean
# N_M = list(map(int, input().split()))
# N = list(map(int, input().split()))
# M = []
# w = [0]*N_M[0]
# N_3 = []
# count = 0
# result = ''

# for i in range(N_M[1]):
#    M = list(map(int, input().split()))
#    count += 1
#    for j in range(M[0]-1,M[1]):
#       w[j] += 1
#       N_3.append(j)
#    if count % 3 == 0:
#       for k in range(len(w)):
#          if k in N_3:
#             w[k] -= 1
#       N_3 = []

# for i in range(len(w)):
#    N[i] += w[i]

# for i in N:
#    result += str(i)
#    result += ' '

# print(result)
#==========================================================================================
n, m = input().split()
home_num = int(n)
rain = int(m)
day = 0

rain_home = [0] * home_num
water = [0] * home_num
home = list(map(int, input().split()))

for _ in range(rain):
	day += 1
	s, e = input().split()
	s = int(s)
	e = int(e)
	
	for idx in range(s-1, e):
		rain_home[idx] += 1
		water[idx] -= 1

	# print('비온 집:', rain_home, day)
	if day % 3 == 0:
		for i in range(home_num):
			if rain_home[i] != 0:
				water[i] += 1
				rain_home[i] = 0  
				
for i in range(len(home)):
    home[i] += abs(water[i])
	
print(' '.join(map(str, home)))
# print(*home) #home이 정수로 이루어진 리스트라서 이렇게 해도 됨_리스트안의 정수 원소들을 문자열로 끄집어내줌

#==========================================================================================
# print(home)
# print(rain_home)
# print(' '.join(str(x + y) for x, y in zip(home, rain_home)))

