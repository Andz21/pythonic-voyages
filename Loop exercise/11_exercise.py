# 11. Print all prime numbers within a range

start, end = input("Enter the start and end of a range with a space: ").split()
start = int(start)
end = int(end)

for num in range(start,end+1):
    if num == 1:
        continue
    elif num in (2,3,5):
        print(num)
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        continue
    else:
        print(num)

