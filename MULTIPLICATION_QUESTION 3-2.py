# multiplication_table.py

# Print the header row
print("  |", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()

# Print the separator row
print("-" * 50)

# Use nested loops to generate the multiplication table
for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()