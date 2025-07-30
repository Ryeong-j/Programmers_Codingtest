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

# print(home)
# print(rain_home)
# print(' '.join(str(x + y) for x, y in zip(home, rain_home)))




# print(' '.join(map(str, home)))


# n, m = input().split()
# home_num=int(n)
# rain=int(m)
# day = 0
# rain_home = [0 * home_num]

# home = list(input().split())
# for i in range(len(home)):
# 	home[i]= int(home[i])

# for i in range(rain):
# 	s, e = input().split()
# 	s= int(s)
# 	e= int(e)

# 	for j in rain_home[s:e+1]:
# 		j += 1

# 	day +=1

# 	if day % 3 == 0:
# 		for k in rain_home:
# 			if k != 0:
# 				home[i] += 1
# 				k = 0

# 	for i, j in zip(rain_home, home):
# 		print(i + j)