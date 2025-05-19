# 14. You have two lists:
# names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78].
# Print these lists as a simple table with columns “Name” and “Score”.

# Solution 1
import pandas as pd

df = pd.DataFrame(data={'Names':["Alice", "Bob", "Charlie"],
                        'Score':[85, 92, 78]})
print(df)


# Solution 2
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{'Name':<10} {'Score':<5}")
print("-" * 15)
for name, score in zip(names, scores):
    print(f"{name:<10} {score:<5}")