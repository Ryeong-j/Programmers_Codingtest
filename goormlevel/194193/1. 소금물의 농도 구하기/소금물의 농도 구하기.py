w1, w2 = input().split()
w1 = int(w1)
w2 = int(w2)

salt = (w1*7) / 100

aa= salt / (w1+w2) * 100 
aa=aa-0.005
print("%.2f" %aa)