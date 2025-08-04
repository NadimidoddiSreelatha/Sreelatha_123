n=input()
r_str=""
for i in range(len(n)-1, -1,-1):
    r_str+=n[i]
print("palindrome"if r_str == n else "Not p")
