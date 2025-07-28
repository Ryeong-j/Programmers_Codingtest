# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
iu = int(input())  

for _ in range(iu):
    a = input()
    parts = a.split() 
	
    x = int(parts[0])
    y = int(parts[1])
    n = int(parts[2])

    b = abs(x) + abs(y)  

    if b <= n and (b % 2 == n % 2):
        print('YES')
    else:
        print('NO')




# user_input = input()
# iu=int(user_input)
# for i in range(iu):
# 	a=input()
# 	print(a)
  
# 	a.split()
# 	b=0
# 	for i in a:
# 		b+=abs(int(i))

# 	if b <= a[2]:
# 		print('YES')
# 	else:
# 		print('NO')
# u = user_input.split()    

# x = int(u[0])
# y = int(u[1])
# n = int(u[2])

# a = abs(x) + abs(y)     

# if a <= n and (a % 2 == n % 2):   
#     print('YES')
# else:
#     print('NO')


# print ("Hello Goorm! Your input is " + user_input)