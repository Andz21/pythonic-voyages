# 17. Find the sum of a series of a number up to n terms

num = int(input("Enter a number: "))
terms = int(input("Enter the terms: "))
# 2 + 22 + 222 + 2222 + 22222

sum = 0
total = 0
for term in range(terms):
    sum = sum * 10 + num
    total += sum

print(f"Sum of the sequence is {total}")
