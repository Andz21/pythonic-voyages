# 7. Accept any three string from one input() call

user_input = input("Enter 3 names separated by space: ")
names = user_input.split(" ")
for i,name in enumerate(names):
    print(f"Name {i+1}: {name}")