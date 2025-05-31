# 3. Create a new string made of the first, middle, and last characters of each input string

s1 = "America"
s2 = "Japan"

s1_mid = len(s1)//2
s2_mid = len(s2)//2

s3 = s1[0] + s2[0] + s1[s1_mid] + s2[s2_mid] + s1[-1] + s2[-1]

print("Mix String is ", s3)