# Write a code to check if two sets have any elements in common. If yes, display the common elements

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if not set1.isdisjoint(set2):
    print("Two sets have items in common")
else:
    print("No items in common")

set3 = set1.intersection(set2)
print(set3)